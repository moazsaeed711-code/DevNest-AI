import tempfile # Create temporary files
import os # File operations
import re # Regular expressions (pattern matching)
from pylint.lint import Run #Execute Pylint
from pylint.reporters.text import TextReporter # Capture Pylint output
from io import StringIO # In-memory text buffer

class PylintAnalyzer:
    def analyze(self, code):
        
        """Run pylint on code and return results"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code) # Writes user's code to temp file
            temp_file = f.name # Saves file path for later use
        
        try:
             # Capture pylint output
            output = StringIO()
            reporter = TextReporter(output)
            
            # Run pylint
            Run([
                temp_file,
                '--disable=C0303,C0304',  # Only disable trailing whitespace and final newline
                '--enable=all',  # Enable all checks
                '--max-line-length=100'
            ], reporter=reporter, exit=False)
            
            pylint_output = output.getvalue()
            print(f"\n{'='*50}")
            print("Pylint raw output:")
            print(pylint_output)
            print(f"{'='*50}\n")
            
            results = self._parse_output(pylint_output)

            print(f"✓ Pylint parsed {len(results)} issues")
            for r in results:
                print(f"  - Line {r['line']}: {r['code']} - {r.get('symbol', 'N/A')}")
            
            return results
            
        except Exception as e:
            print(f"❌ Pylint analysis error: {e}")
            import traceback
            traceback.print_exc()
            return []
        
        finally:
            if os.path.exists(temp_file):
                try:
                    os.unlink(temp_file)
                except:
                    pass
    
    def _parse_output(self, output):
        """Parse pylint output into structured format"""
        issues = [] # Creates empty list to store parsed issues.
         
        # Split into lines
        lines = output.split('\n')
        
        for line in lines:
            # Pattern: "file.py:10:0: E0602: Undefined variable 'undefined_variable' (undefined-variable)"
            # Pattern: "file.py:1:0: W0611: Unused import os (unused-import)"
            
            # Use regex to match pylint output format
            match = re.search(r':(\d+):\d+:\s*([EWCRF]\d{4}):\s*(.+?)\s*\(([^)]+)\)', line)
            
            if match:
                line_num = int(match.group(1))
                code = match.group(2)
                message = match.group(3)
                symbol_name = match.group(4)
                
                # Extract variable/symbol name from message
                symbol = self._extract_symbol_from_message(message)
                
                issues.append({
                    'line': line_num,
                    'code': code,
                    'message': message,
                    'symbol': symbol
                })
                
                print(f"  ✓ Parsed: Line {line_num}, Code {code}, Symbol: {symbol}")
        
        return issues
    
    def _extract_symbol_from_message(self, message):
        """Extract variable/function name from message"""
        
        # Try double quotes first (Pylint sometimes uses these)
        match = re.search(r'"([^"]+)"', message)
        if match:
            return match.group(1)
        
        # Try single quotes
        match = re.search(r"'([^']+)'", message)
        if match:
            return match.group(1)
        
        # Look for "name X" patterns
        patterns = [
            r'name\s+"([^"]+)"',
            r"name\s+'([^']+)'",
            r'Constant\s+name\s+"([^"]+)"',
            r'Variable\s+name\s+"([^"]+)"',
            r'Function\s+name\s+"([^"]+)"',
            r'Class\s+name\s+"([^"]+)"',
            r'Argument\s+name\s+"([^"]+)"',
            r'Method\s+name\s+"([^"]+)"'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                return match.group(1)
        
        # Look for common patterns
        if 'variable ' in message.lower():
            words = message.split()
            for i, word in enumerate(words):
                if word.lower() == 'variable' and i + 1 < len(words):
                    return words[i + 1].strip("'\"(),")
        
        if 'import ' in message.lower():
            words = message.split()
            for i, word in enumerate(words):
                if word.lower() == 'import' and i + 1 < len(words):
                    return words[i + 1].strip("'\"(),")
        
        return None