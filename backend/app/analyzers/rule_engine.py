"""
Enhanced Rule Engine for DevNest
Translates Pylint error codes into beginner-friendly educational messages
Enhanced with organized, emoji-rich format for better learning experience
"""

class RuleEngine:
    def __init__(self):
        """
        Initialize the Rule Engine with comprehensive error translations
        Enhanced with structured learning format
        """
       
# ============================================================================
# ERROR CODE MAPPINGS - Organized by Category
# ============================================================================
        self.error_rules = {


    # ========================================
    # CRITICAL ERRORS (E0xxx - E1xxx)
    # ========================================
    
    # Additional Common Runtime Errors
    'E0012': 'bad-option-value',           # Bad option value
    'E0239': 'inherit-non-class',          # Inheriting from non-class
    'E0240': 'inconsistent-mro',           # Method Resolution Order problem
    'E1003': 'bad-super-call',             # Bad super() call
    'E1004': 'missing-super-argument',     # Missing argument in super()
    'E1140': 'unhashable-dict-key',        # Unhashable dict key
    'E1141': 'dict-iter-missing-items',    # Iterating dict without .items()
    'E1142': 'await-outside-async',        # await outside async function
    'E1143': 'invalid-context-manager',    # Invalid __enter__/__exit__

    # String/Bytes Errors
    'E1307': 'bad-string-format-type',     # Wrong type in format string
    'E1310': 'bad-str-strip-call',         # Bad str.strip() call
    'E1700': 'yield-inside-async-function', # yield in async function
    'E1701': 'not-async-context-manager',  # Not an async context manager

    # Comparison Errors  

    'E0106': 'return-arg-in-generator',    # return with argument inside generator
    'E0117': 'nonlocal-and-global',        # nonlocal and global in same scope


    # E00xx - Syntax and Basic Errors
    'E0001': 'syntax-error',
    'E0011': 'bad-indentation',
    
    # E01xx - Class/Function Definition Errors
    'E0100': 'init-is-generator',
    'E0102': 'function-redefined',
    'E0103': 'not-in-loop',
    'E0104': 'return-outside-function',
    'E0105': 'yield-outside-function',
    'E0107': 'nonexistent-operator',
    'E0108': 'duplicate-argument-name',
    'E0110': 'abstract-class-instantiated',
    
    # E02xx - Class/Method Errors
    'E0202': 'method-hidden',
    'E0203': 'access-member-before-definition',
    'E0211': 'no-method-argument',
    'E0213': 'no-self-argument',
    'E0236': 'invalid-slots-object',
    'E0237': 'assigning-non-slot',
    'E0241': 'duplicate-bases',
    
    # E03xx - Iterator/Special Method Errors
    'E0301': 'non-iterator-returned',
    'E0302': 'unexpected-special-method-signature',
    'E0303': 'invalid-length-returned',
    
    # E04xx - Import Errors
    'E0401': 'import-error',
    
    # E06xx - Variable Errors
    'E0601': 'used-before-assignment',
    'E0602': 'undefined-variable',
    'E0611': 'no-name-in-module',
    
    # E10xx - Type/Object Errors
    'E1101': 'no-member',
    'E1102': 'not-callable',
    'E1111': 'assignment-from-no-return',
    'E1120': 'no-value-for-parameter',
    'E1121': 'too-many-function-args',
    'E1123': 'unexpected-keyword-arg',
    'E1124': 'redundant-keyword-arg',
    'E1125': 'missing-kwoa',
    'E1126': 'invalid-sequence-index',
    'E1127': 'invalid-slice-index',
    'E1128': 'assignment-from-none',
    'E1129': 'not-context-manager',
    'E1130': 'invalid-unary-operand-type',
    'E1131': 'unsupported-binary-operation',
    'E1132': 'repeated-keyword',
    'E1133': 'not-an-iterable',
    'E1134': 'not-a-mapping',
    'E1135': 'unsupported-membership-test',
    'E1136': 'unsubscriptable-object',
    'E1137': 'unsupported-assignment-operation',
    'E1138': 'unsupported-delete-operation',
    'E1139': 'invalid-metaclass',
    
    # E12xx - Logging Errors
    'E1200': 'logging-unsupported-format',
    'E1205': 'logging-too-many-args',
    'E1206': 'logging-too-few-args',
    
    # ========================================
    # WARNINGS (W0xxx - W1xxx)
    # ========================================
    
    # W01xx - Code Logic Warnings
    'W0101': 'unreachable',
    'W0102': 'dangerous-default-value',
    'W0104': 'pointless-statement',
    'W0105': 'pointless-string-statement',
    'W0106': 'expression-not-assigned',
    'W0107': 'unnecessary-pass',
    'W0108': 'unnecessary-lambda',
    'W0109': 'duplicate-key',
    
    # W01xx - Dangerous Code
    'W0122': 'exec-used',
    'W0123': 'eval-used',
    'W0124': 'confusing-with-statement',
    'W0125': 'using-constant-test',
    'W0150': 'lost-exception',
    'W0160': 'consider-using-enumerate',
    'W0199': 'assert-on-tuple',
    
    # W02xx - Class/Method Warnings
    'W0201': 'attribute-defined-outside-init',
    'W0211': 'bad-staticmethod-argument',
    'W0212': 'protected-access',
    'W0221': 'arguments-differ',
    'W0222': 'signature-differs',
    'W0223': 'abstract-method',
    'W0231': 'super-init-not-called',
    'W0232': 'no-init',
    'W0233': 'non-parent-init-called',
    'W0235': 'useless-super-delegation',
    
    # W03xx - Semicolons and Indentation
    'W0301': 'unnecessary-semicolon',
    'W0311': 'bad-indentation',
    
    # W04xx - Import Warnings
    'W0401': 'wildcard-import',
    'W0404': 'reimported',
    'W0406': 'import-self',
    'W0410': 'misplaced-future',
    
    # W05xx - Comments
    'W0511': 'fixme',
    
    # W06xx - Variable Scope Warnings
    'W0601': 'global-variable-undefined',
    'W0602': 'global-variable-not-assigned',
    'W0603': 'global-statement',
    'W0611': 'unused-import',
    'W0612': 'unused-variable',
    'W0613': 'unused-argument',
    'W0614': 'unused-wildcard-import',
    'W0621': 'redefined-outer-name',
    'W0622': 'redefined-builtin',
    'W0631': 'undefined-loop-variable',
    'W0632': 'unbalanced-tuple-unpacking',
    'W0633': 'unpacking-non-sequence',
    'W0640': 'cell-var-from-loop',
    
    # W07xx - Exception Warnings
    'W0702': 'bare-except',
    'W0718': 'broad-exception-caught',
    
    # W11xx - Argument/Parameter Warnings
    'W1113': 'keyword-arg-before-vararg',
    
    # W12xx - Logging/Format Warnings
    'W1201': 'logging-not-lazy',
    'W1202': 'logging-format-interpolation',
    'W1203': 'logging-fstring-interpolation',
    
    # W13xx - String Format Warnings
    'W1300': 'bad-format-string',
    'W1301': 'unused-format-string-argument',
    'W1302': 'bad-format-string-key',
    'W1303': 'missing-format-argument-key',
    'W1305': 'format-combined-specification',
    'W1309': 'f-string-without-interpolation',
    
    # W14xx - String Content Warnings
    'W1401': 'anomalous-backslash-in-string',
    
    # W15xx - File/Resource Warnings
    'W1501': 'bad-open-mode',
    'W1503': 'redundant-unittest-assert',
    'W1514': 'unspecified-encoding',

    'W0143': 'comparison-with-callable',    # Comparison with callable
    'W0177': 'redeclared-assigned-name',   # Variable redeclared
    'W0211': 'bad-staticmethod-argument',   # Already exists
    'W0237': 'arguments-renamed',          # Arguments renamed in override
    'W0238': 'unused-private-member',      # Unused private member
    'W0246': 'useless-parent-delegation',  # Useless parent delegation

    # Format String Warnings
    'W1304': 'format-needs-mapping',       # Format string needs mapping
    'W1306': 'missing-format-string-key',  # Missing key in format string
    'W1308': 'duplicate-string-formatting-argument',  # Duplicate format arg
    'W1310': 'format-string-without-interpolation',   # No interpolation
    
    # ========================================
    # CONVENTIONS (C0xxx - C4xxx)
    # ========================================
    
    # C01xx - Naming and Documentation
    'C0102': 'blacklisted-name',
    'C0103': 'invalid-name',
    'C0104': 'disallowed-name',
    'C0112': 'empty-docstring',
    'C0113': 'unneeded-not',
    'C0114': 'missing-module-docstring',
    'C0116': 'missing-function-docstring',
    'C0121': 'singleton-comparison',
    'C0123': 'unidiomatic-typecheck',
    
    # C02xx - Class Method Conventions
    'C0200': 'consider-using-enumerate',
    'C0201': 'consider-iterating-dictionary',
    'C0202': 'bad-classmethod-argument',
    'C0203': 'bad-mcs-method-argument',
    'C0204': 'bad-mcs-classmethod-argument',
    'C0205': 'single-string-used-for-slots',
    'C0208': 'use-sequence-for-iteration',
    'C0209': 'consider-using-f-string',
    
    # C03xx - Formatting Conventions
    'C0301': 'line-too-long',
    'C0302': 'too-many-lines',
    'C0303': 'trailing-whitespace',
    'C0304': 'missing-final-newline',
    'C0321': 'multiple-statements',
    'C0325': 'superfluous-parens',
    'C0326': 'bad-whitespace',
    'C0327': 'mixed-line-endings',
    'C0328': 'unexpected-line-ending-format',
    
    # C04xx - Import Conventions
    'C0410': 'multiple-imports',
    'C0411': 'wrong-import-order',
    'C0412': 'ungrouped-imports',
    'C0413': 'wrong-import-position',
    'C0414': 'useless-import-alias',
    'C0415': 'import-outside-toplevel',

    'C0115': 'missing-class-docstring',    # Missing class docstring
    'C0131': 'typevar-double-variance',    # TypeVar double variance
    'C0132': 'typevar-name-mismatch',      # TypeVar name mismatch
    'C0206': 'consider-using-dict-items',  # Use dict.items()
    'C0207': 'use-maxsplit-arg',           # Use maxsplit in str.split()
    'C1805': 'invalid-sequence-index',     # Invalid sequence index
    
    # ========================================
    # REFACTORING (R0xxx - R1xxx)
    # ========================================
    
    # R02xx - Design Refactoring
    'R0201': 'no-self-use',
    'R0202': 'no-classmethod-decorator',
    'R0203': 'no-staticmethod-decorator',
    'R0205': 'useless-object-inheritance',
    'R0206': 'property-with-parameters',
    
    # R04xx - Dependency Refactoring
    'R0401': 'cyclic-import',
    
    # R08xx - Code Duplication
    'R0801': 'duplicate-code',
    
    # R09xx - Complexity Refactoring
    'R0902': 'too-many-instance-attributes',
    'R0903': 'too-few-public-methods',
    'R0911': 'too-many-return-statements',
    'R0912': 'too-many-branches',
    'R0913': 'too-many-arguments',
    'R0914': 'too-many-locals',
    'R0915': 'too-many-statements',
    'R0916': 'too-many-boolean-expressions',
    
    # R17xx - Code Simplification
    'R1701': 'consider-merging-isinstance',
    'R1702': 'too-many-nested-blocks',
    'R1703': 'simplifiable-if-expression',
    'R1704': 'redefined-argument-from-local',
    'R1705': 'no-else-return',
    'R1706': 'consider-using-ternary',
    'R1707': 'trailing-comma-tuple',
    'R1708': 'stop-iteration-return',
    'R1709': 'simplify-boolean-expression',
    'R1710': 'inconsistent-return-statements',
    'R1711': 'useless-return',
    'R1712': 'consider-swap-variables',
    'R1713': 'consider-using-join',
    'R1714': 'consider-using-in',
    'R1715': 'consider-using-get',
    'R1716': 'chained-comparison',
    'R1717': 'consider-using-dict-comprehension',
    'R1718': 'consider-using-set-comprehension',
    'R1719': 'simplifiable-if-statement',
    'R1720': 'no-else-raise',
    'R1721': 'unnecessary-comprehension',
    'R1722': 'consider-using-sys-exit',
    'R1723': 'no-else-break',
    'R1724': 'no-else-continue',
    'R1725': 'super-with-arguments',
    'R1726': 'simplifiable-condition',
    'R1727': 'condition-evals-to-constant',
    'R1728': 'consider-using-generator',
    'R1729': 'use-a-generator',
    'R1730': 'consider-using-min-builtin',
    'R1731': 'consider-using-max-builtin',
    'R1732': 'consider-using-with',
    'R1733': 'unnecessary-dict-index-lookup',
    'R1734': 'use-list-literal',
    'R1735': 'use-dict-literal',
    'R0124': 'comparison-with-itself',     # Comparing with itself
    'R1260': 'too-complex',                # McCabe complexity too high
    'R1702': 'too-many-nested-blocks',     # Already exists
    'R1736': 'unnecessary-list-index-lookup',  # Unnecessary list indexing
    'R6002': 'consider-using-alias',       # Consider using type alias
    'R6003': 'consider-alternative-union-syntax',  # Use | instead of Union
}


# ============================================================================
# DETAILED EXPLANATIONS - Organized by Severity
# ============================================================================

        self.explanations = {

    # ============================================
    # CRITICAL ERRORS (Must Fix!)
    # ============================================
    
    'undefined-variable': {
        'title': "🚨 Undefined Variable Error",
        'explain': "You're trying to use the variable '{symbol}' before defining it. In Python, every variable must be created (assigned a value) before you can use it. This error means Python has never seen '{symbol}' before this line. It's like trying to read a book that hasn't been written yet - Python doesn't know what '{symbol}' is supposed to be!",
        'how_to_fix': "Create the variable before using it:\n1. Add a line BEFORE this error that assigns a value to '{symbol}'\n2. Make sure the variable name is spelled exactly the same\n3. Check that it's in the right scope (inside vs outside functions)",
        'wrong': "print(name)  # Error: name doesn't exist yet!",
        'right': "name = 'Alice'  # Define it first\nprint(name)  # Now it works!",
        'learn': "💡 Variables must be assigned before use. Think of it like trying to open a box that doesn't exist yet - you need to create the box first! Python reads code top-to-bottom, so definitions must come before usage.",
        'severity': 'error'
    },
    
   'used-before-assignment': {
        'title': "🚨 Variable Used Before Assignment",
        'explain': "The variable '{symbol}' is being used in an operation (like += or comparison) before it has been given an initial value in this function or scope. This is different from undefined - Python knows the name exists somewhere, but it hasn't been set up with a starting value in THIS specific place. It's like trying to add 10 to a number before deciding what that number is!",
        'how_to_fix': "Initialize the variable with a starting value:\n1. Add a line that gives '{symbol}' its first value (like = 0 for numbers, = [] for lists)\n2. Put this BEFORE you try to modify it with += or similar operations\n3. Remember: each function needs its own initialization",
        'wrong': "def calculate():\n    total += 10  # Error: total doesn't exist yet!",
        'right': "def calculate():\n    total = 0  # Initialize first\n    total += 10  # Now it works!",
        'learn': "💡 Think of variables like empty jars. You can't put MORE cookies in a jar that doesn't exist yet! You need to create the jar (initialize) before you can add to it (+=). Variables from outside functions aren't automatically available inside!",
        'severity': 'error'
    },
    
    'syntax-error': {
        'title': "🚨 Syntax Error",
        'explain': "Python couldn't understand this line because there's a grammatical mistake in your code. Syntax errors are like typos or missing punctuation in English - they make it impossible for Python to read your code. Common causes: missing colons after if/for/def, unclosed parentheses or quotes, wrong indentation (spaces/tabs), or using Python keywords incorrectly.",
        'how_to_fix': "Check these common syntax mistakes:\n1. Missing colon (:) after if, for, while, def, class\n2. Unclosed parentheses ( ), brackets [ ], or quotes \" \"\n3. Indentation problems (mixing tabs and spaces)\n4. Using = instead of == in conditions",
        'wrong': "if age > 18\n    print('Adult')  # Missing colon!",
        'right': "if age > 18:\n    print('Adult')  # Colon added!",
        'learn': "💡 Syntax errors are like grammar mistakes in English - they make your code impossible to understand. Python is very picky about punctuation and structure! The good news: they're usually easy to spot and fix.",
        'severity': 'error'
    },
    
    'no-member': {
        'title': "🚨 Attribute/Method Not Found",
        'explain': "You're trying to use an attribute or method ('{symbol}') that doesn't exist for this type of object. Different data types have different capabilities - for example, lists have append(), but strings don't. It's like trying to use a car key on a house door - wrong tool for the job! Python is telling you this object doesn't have the feature you're looking for.",
        'how_to_fix': "Match the method to the object type:\n1. Check what type of object you have (use type() or print())\n2. Look up what methods that type supports (use dir(object) or online docs)\n3. Use the correct method for that type (strings use +, lists use append())\n4. Check for typos in the method name",
        'wrong': "text = 'hello'\ntext.append('!')  # Strings don't have append()!",
        'right': "text = 'hello'\ntext = text + '!'  # Use + for strings\n# OR\nitems = ['hello']\nitems.append('!')  # Lists DO have append()",
        'learn': "💡 Different object types are like different tools - each has its own features. Lists have append(), strings have upper(), numbers have math operations. You can't hammer a nail with a screwdriver! Use help(object) or dir(object) to see what's available.",
        'severity': 'error'
    },
    
    'import-error': {
        'title': "🚨 Import Error - Module Not Found",
        'explain': "Python cannot find the module '{symbol}' that you're trying to import. This happens for three main reasons: 1) The module isn't installed on your computer, 2) You misspelled the module name, or 3) You're trying to import your own file but it's in the wrong location. It's like trying to open a program that isn't installed on your computer - Python can't use what it can't find!",
        'how_to_fix': "Find and fix the import problem:\n1. For external packages: Install with 'pip install {symbol}' in terminal/command prompt\n2. For built-in modules: Check spelling carefully (it's case-sensitive!)\n3. For your own files: Make sure the file is in the same folder\n4. Verify the package name (some have different names: cv2 installs as opencv-python)",
        'wrong': "import nonexistent_module  # Not installed!",
        'right': "# For built-in modules (already installed):\nimport os\nimport math\n\n# For external packages (install first):\n# In terminal: pip install requests\nimport requests",
        'learn': "💡 Python has built-in modules (already installed) and external packages (need pip install). Think of it like apps on your phone - some come pre-installed, others you need to download from the app store! Always check if you need to install something first.",
        'severity': 'error'
    },
    
    'no-value-for-parameter': {
        'title': "🚨 Missing Required Argument",
        'explain': "You're calling a function without providing all required arguments.",
        'how_to_fix': "Check the function definition and provide all required parameters.",
        'wrong': "def greet(name, age):\n    print(f'{name} is {age}')\n\ngreet('Alice')  # Missing age!",
        'right': "def greet(name, age):\n    print(f'{name} is {age}')\n\ngreet('Alice', 25)  # All arguments provided",
        'learn': "💡 Functions need all their parameters unless they have default values!",
        'severity': 'error'
    },
    
    'too-many-function-args': {
        'title': "🚨 Too Many Arguments",
        'explain': "You're providing more arguments than the function accepts.",
        'how_to_fix': "Check how many parameters the function expects and match them.",
        'wrong': "def add(a, b):\n    return a + b\n\nresult = add(1, 2, 3)  # Too many!",
        'right': "def add(a, b):\n    return a + b\n\nresult = add(1, 2)  # Correct number",
        'learn': "💡 Count your function parameters and match your arguments!",
        'severity': 'error'
    },
    
    'no-name-in-module': {
        'title': "🚨 Name Not Found in Module",
        'explain': "You're trying to import '{symbol}' from a module, but that name doesn't exist in that module! This usually happens because: 1) You misspelled the name (cosine vs cos), 2) You're using the wrong module version (the name was renamed or removed), or 3) You're confusing similar names. It's like asking for a specific tool from a toolbox that doesn't have it - you need to check what's actually in there!",
        'how_to_fix': "Find the correct name:\n1. Check the module's official documentation\n2. Use dir(module) to list all available names after importing the module\n3. Use help(module) to see detailed documentation\n4. Check for typos (common: cos vs cosine, sqrt vs squareroot)\n5. Verify you have the right module version",
        'wrong': "from math import cosine  # No 'cosine' in math!\nfrom os import getcwd_path  # Wrong name!\nfrom datetime import DateTime  # Wrong case!",
        'right': "from math import cos  # Correct name\nfrom os import getcwd  # Correct name\nfrom datetime import datetime  # Correct case\n\n# To discover what's available:\nimport math\nprint(dir(math))  # Shows all available items",
        'learn': "💡 Module documentation is your friend! Every module has specific names for its functions and classes. Use dir(module) to explore what's available - it's like reading the menu before ordering. Python is case-sensitive, so 'DateTime' and 'datetime' are different. When in doubt, check the docs!",
        'severity': 'error'
    },
    
    'function-redefined': {
        'title': "🚨 Function Redefined - Duplicate Name",
        'explain': "You've defined the same function name twice in the same scope. Python doesn't give an error for this, but it's almost always a mistake! The second definition completely replaces the first one - the original function is gone, as if it never existed. This is confusing because someone might call the function expecting the first version's behavior but get the second version instead. It's like labeling two different tools with the same name in your toolbox!",
        'how_to_fix': "Choose a solution based on your intent:\n1. If they're different functions: Give them unique, descriptive names (calculate_sum vs calculate_average)\n2. If the second is an improved version: Remove the old definition entirely\n3. If they handle different cases: Combine them into one function with parameters\n4. Use version suffixes only if absolutely necessary (_v1, _v2)",
        'wrong': "def calculate():\n    return 1\n\ndef calculate():  # Overwrites the first completely!\n    return 2\n\nprint(calculate())  # Always prints 2, first version is lost\n\ndef greet():\n    return 'Hello'\n\ndef greet():  # Duplicate again!\n    return 'Hi'",
        'right': "def calculate_sum():\n    return 1\n\ndef calculate_average():\n    return 2\n\n# OR combine into one:\ndef calculate(operation):\n    if operation == 'sum':\n        return 1\n    elif operation == 'average':\n        return 2\n\n# OR if truly improving:\ndef greet():  # Only define once, final version\n    return 'Hi'",
        'learn': "💡 Each function name should be unique in its scope! When you redefine a function, Python silently replaces it - no warning, no error. This is different from variables where reassignment is normal. Function names are supposed to be permanent labels. Think of it like having two books with the same title on your shelf - very confusing! Use meaningful, distinct names.",
        'severity': 'error'
    },
    
    'not-in-loop': {
        'title': "🚨 Break/Continue Outside Loop",
        'explain': "You're using 'break' or 'continue' but you're not inside a for or while loop! These keywords only make sense inside loops: 'break' exits the loop entirely, 'continue' skips to the next iteration. Using them outside a loop is like pressing the 'Next Song' button when no music is playing - the command has no context. Python will crash with a SyntaxError if you try to run this.",
        'how_to_fix': "Fix the structure:\n1. If you need to exit early from a condition, use 'return' in a function or restructure your logic\n2. Make sure break/continue are INSIDE the loop body (indented under for/while)\n3. Check your indentation - if break/continue aren't indented properly, they're not in the loop\n4. If you're trying to exit nested blocks, consider using functions and return instead",
        'wrong': "if condition:\n    break  # Not in a loop - ERROR!\n\nfor item in items:\n    process(item)\nbreak  # Outside the loop - ERROR!\n\nif x > 10:\n    continue  # Not in a loop - ERROR!",
        'right': "# break inside loop:\nfor item in items:\n    if condition:\n        break  # Exits the loop\n\n# continue inside loop:\nfor item in items:\n    if should_skip(item):\n        continue  # Skips to next item\n    process(item)\n\n# For early exit from conditions, use return:\ndef check_items(items):\n    if not items:\n        return None  # Exit function early\n    return process(items)",
        'learn': "💡 break and continue are loop control keywords - they only exist to control loops! break says 'stop the loop completely', continue says 'skip the rest of this iteration'. Think of a loop like a race track: break means 'leave the track', continue means 'skip to next lap'. You can't do either if you're not on the track! Always make sure these keywords are indented inside your for/while blocks.",
        'severity': 'error'
    },
    
    'return-outside-function': {
        'title': "🚨 Return Statement Outside Function",
        'explain': "You're using 'return' outside of any function definition. The 'return' keyword only makes sense inside a function because its job is to send a value back to whoever called that function. Using it at the top level of your script is like trying to give someone their change when they never made a purchase - there's no transaction to complete! Python will crash with a SyntaxError when it sees this.",
        'how_to_fix': "Move code into a function:\n1. Wrap your code in a function definition: def main():\n2. Put the return statement inside that function\n3. Call the function at the bottom: if __name__ == '__main__': main()\n4. Or if you're not actually returning to anything, just remove the return statement\n5. For scripts, you might not need return at all - the script just ends naturally",
        'wrong': "# At the top level of a script:\nresult = 5 * 10\nreturn result  # ERROR: Not in a function!\n\nx = calculate_something()\nreturn x  # ERROR: Can't return from script!\n\nif condition:\n    return True  # ERROR: Not in a function!",
        'right': "# Put code in a function:\ndef calculate():\n    result = 5 * 10\n    return result  # Now it makes sense!\n\n# Call the function:\nanswer = calculate()\nprint(answer)\n\n# OR for scripts that don't return:\ndef main():\n    result = 5 * 10\n    print(result)  # Just use the value\n\nif __name__ == '__main__':\n    main()",
        'learn': "💡 'return' is a function's way of saying 'here's my answer'. You can only give an answer if someone asked a question (called your function)! Top-level script code just runs and ends - there's no one to return to. Think of return like handing in homework - you need a teacher (function caller) to hand it to. If you're writing a script, structure it with functions and call them, or just let it run without returns.",
        'severity': 'error'
    },
    
    'yield-outside-function': {
        'title': "🚨 Yield Outside Function",
        'explain': "'yield' can only be used inside a function to create a generator.",
        'how_to_fix': "Put yield inside a function definition.",
        'wrong': "yield 42  # Not in a function!",
        'right': "def my_generator():\n    yield 42  # Inside function!",
        'learn': "💡 yield creates generators, which must be defined as functions!",
        'severity': 'error'
    },
    
    'duplicate-argument-name': {
        'title': "🚨 Duplicate Function Parameter",
        'explain': "You have the same parameter name twice in the function definition.",
        'how_to_fix': "Use unique names for each parameter.",
        'wrong': "def greet(name, name):  # Duplicate!",
        'right': "def greet(first_name, last_name):  # Unique names",
        'learn': "💡 Each parameter needs a unique name so you can tell them apart!",
        'severity': 'error'
    },
    
    'no-method-argument': {
        'title': "🚨 Method Missing 'self' Parameter",
        'explain': "Instance methods in a class must have 'self' as the first parameter.",
        'how_to_fix': "Add 'self' as the first parameter.",
        'wrong': "class MyClass:\n    def greet():  # Missing self!",
        'right': "class MyClass:\n    def greet(self):  # Has self!",
        'learn': "💡 'self' represents the instance - it's how methods access the object's data!",
        'severity': 'error'
    },
    
    'no-self-argument': {
        'title': "🚨 First Parameter Should Be 'self'",
        'explain': "By convention, the first parameter of an instance method should be named 'self'.",
        'how_to_fix': "Rename the first parameter to 'self'.",
        'wrong': "class MyClass:\n    def greet(this):  # Should be 'self'",
        'right': "class MyClass:\n    def greet(self):  # Python convention",
        'learn': "💡 While 'this' works, 'self' is the Python convention everyone follows!",
        'severity': 'error'
    },
    
    'not-callable': {
        'title': "🚨 Object is Not Callable",
        'explain': "You're trying to call something that isn't a function. This often happens when you use parentheses on a non-function object.",
        'how_to_fix': "Check if you're trying to call a variable, list, or other non-function object.",
        'wrong': "my_list = [1, 2, 3]\nresult = my_list()  # Lists aren't callable!",
        'right': "my_list = [1, 2, 3]\nresult = my_list[0]  # Access with []",
        'learn': "💡 Only functions, methods, and classes can be called with (). Check your variable names carefully!",
        'severity': 'error'
    },
    
    'not-an-iterable': {
        'title': "🚨 Object is Not Iterable",
        'explain': "You're trying to loop over something that can't be looped over.",
        'how_to_fix': "Make sure you're looping over a list, tuple, string, range, or other iterable object.",
        'wrong': "for item in 5:  # Can't loop over a number!\n    print(item)",
        'right': "for item in range(5):  # Loop over range\n    print(item)",
        'learn': "💡 Only sequences (lists, strings, ranges, etc.) can be used in for loops!",
        'severity': 'error'
    },
    
    'not-context-manager': {
        'title': "🚨 Object Not a Context Manager",
        'explain': "You're using 'with' on an object that doesn't support the with statement.",
        'how_to_fix': "Only use 'with' on objects that support it (files, locks, etc.).",
        'wrong': "with 42:  # Numbers don't support 'with'!",
        'right': "with open('file.txt') as f:  # Files support 'with'",
        'learn': "💡 The 'with' statement is for objects that need setup and cleanup, like files!",
        'severity': 'error'
    },
    
    'unexpected-keyword-arg': {
        'title': "🚨 Unexpected Keyword Argument",
        'explain': "You're passing a keyword argument that the function doesn't accept.",
        'how_to_fix': "Check the function signature for accepted parameter names.",
        'wrong': "def greet(name):\n    print(name)\ngreet(age=25)  # 'age' not accepted!",
        'right': "def greet(name):\n    print(name)\ngreet(name='Alice')  # Correct parameter",
        'learn': "💡 Keyword arguments must match the function's parameter names!",
        'severity': 'error'
    },
    
    'unsubscriptable-object': {
        'title': "🚨 Object Cannot Be Indexed",
        'explain': "You're trying to use [] on an object that doesn't support indexing.",
        'how_to_fix': "Only use [] on sequences (lists, strings, tuples) and dictionaries.",
        'wrong': "number = 42\ndigit = number[0]  # Numbers don't support indexing!",
        'right': "text = '42'\ndigit = text[0]  # Strings support indexing",
        'learn': "💡 Only sequences and mappings can be accessed with []!",
        'severity': 'error'
    },
    
    'bad-indentation': {
        'title': "🚨 Incorrect Indentation",
        'explain': "Python uses indentation (spaces at the start of lines) to define code structure and blocks - it's not optional formatting like in other languages! Your code has inconsistent or incorrect indentation, which Python can't understand. Common causes: mixing tabs and spaces, wrong number of spaces, or forgetting to indent after colons (:). It's like trying to read a book where some paragraphs randomly start at different margins - impossible to follow!",
        'how_to_fix': "Fix your indentation:\n1. Use 4 spaces for each indentation level (Python standard)\n2. Never mix tabs and spaces - choose one (spaces recommended)\n3. After : (if, for, def, class), indent the next line\n4. All lines in the same block must have the same indentation\n5. Configure your editor to show whitespace and convert tabs to spaces",
        'wrong': "if True:\nprint('hello')  # Error: not indented!\n\ndef calculate():\n  return 1  # Inconsistent: 2 spaces\n    \nfor i in range(3):\n      print(i)  # Inconsistent: 6 spaces",
        'right': "if True:\n    print('hello')  # Correct: 4 spaces\n\ndef calculate():\n    return 1  # Consistent: 4 spaces\n    \nfor i in range(3):\n    print(i)  # Consistent: 4 spaces\n\n# Nested blocks:\nif True:\n    if True:\n        print('nested')  # 8 spaces (2 levels)",
        'learn': "💡 Python's indentation isn't just style - it's syntax! While other languages use {} braces, Python uses whitespace to show structure. This forces readable code but means indentation errors break your program. Always use 4 spaces per level - it's the universal Python standard (PEP 8). Set your editor to convert tabs to 4 spaces automatically. Think of indentation as visual hierarchy that Python actually understands!",
        'severity': 'error'
    },
    
    'assignment-from-no-return': {
        'title': "🚨 Assigning from Function with No Return",
        'explain': "You're assigning a variable to the result of a function that doesn't return any value (no return statement). In Python, functions without explicit return automatically return None. So you're essentially doing 'result = None' in a confusing way. This usually means: 1) You forgot to add return to the function, or 2) You're trying to capture a side effect (like print) which doesn't work. It's like asking someone for their answer after they just nodded without speaking!",
        'how_to_fix': "Choose the right fix:\n1. Add return statement to the function: return the value you want\n2. Don't assign if the function works by side effects (like print, append)\n3. Check if you meant to call a different function that does return something\n4. Remember: print() returns None, it doesn't return what it prints",
        'wrong': "def process_data(data):\n    print(data)  # No return!\n    data.append(1)  # Side effect\n\nresult = process_data([1, 2])  # result is None\nprint(result)  # Prints: None\n\ndef calculate():\n    x = 5 * 10  # Forgot return!\n    \ntotal = calculate()  # total is None",
        'right': "def process_data(data):\n    data.append(1)\n    return data  # Return the modified data\n\nresult = process_data([1, 2])  # result is [1, 2, 1]\n\ndef calculate():\n    x = 5 * 10\n    return x  # Return the value\n    \ntotal = calculate()  # total is 50\n\n# OR if function is only for side effects:\ndef log_message(msg):\n    print(msg)  # Just prints, doesn't return\n    \nlog_message('Hello')  # Don't assign it",
        'learn': "💡 Functions without 'return' automatically return None! This is different from some languages where the last expression is returned. In Python, you must explicitly return values. If a function modifies something (side effect) vs. calculating something (return value), that's a key design choice. print() and append() work by side effects - they return None. Always ask: 'Does this function give me back a value, or just do something?'",
        'severity': 'error'
    },
    
    'init-is-generator': {
        'title': "🚨 __init__ Cannot Be a Generator",
        'explain': "The __init__ method cannot use 'yield' - it must return None.",
        'how_to_fix': "Remove yield from __init__, or create a separate generator method.",
        'wrong': "class MyClass:\n    def __init__(self):\n        yield 1  # Not allowed!",
        'right': "class MyClass:\n    def __init__(self):\n        self.value = 1  # No yield",
        'learn': "💡 __init__ initializes objects, it can't be a generator!",
        'severity': 'error'
    },
    
    'invalid-sequence-index': {
        'title': "🚨 Invalid Index Type",
        'explain': "You're trying to use a non-integer value (like a string or float) to index into a list or tuple. In Python, sequence indices MUST be integers (or slices). This error often happens when: 1) You accidentally put quotes around a number ('0' instead of 0), 2) You're using a number read from input (which is a string), or 3) You're thinking of dictionaries which can have string keys. It's like trying to find apartment number 'five' instead of apartment 5!",
        'how_to_fix': "Convert to integer or fix the type:\n1. Remove quotes: items['0'] → items[0]\n2. Convert strings: items[int(index_str)]\n3. Convert floats: items[int(3.5)] (rounds down)\n4. For user input: always int() it before using as index\n5. For string keys, use dictionaries not lists",
        'wrong': "items = [10, 20, 30]\nvalue = items['0']  # TypeError: string index!\nvalue = items[1.5]  # TypeError: float index!\n\n# From user input:\nindex = input('Enter index: ')  # Returns string!\nvalue = items[index]  # TypeError!\n\ndata = ['a', 'b', 'c']\nresult = data['b']  # TypeError: strings are not valid indices",
        'right': "items = [10, 20, 30]\nvalue = items[0]  # Correct: integer\nvalue = items[int(1.5)]  # Correct: convert float\n\n# From user input:\nindex = input('Enter index: ')\nvalue = items[int(index)]  # Convert to int first!\n\n# For string keys, use dict:\ndata = {'a': 1, 'b': 2, 'c': 3}\nresult = data['b']  # Correct: dicts can have string keys",
        'learn': "💡 Lists and tuples use integer positions (0, 1, 2...) while dictionaries use keys (can be strings). Don't confuse them! When you get input from users with input(), it's always a string - convert with int() before using as an index. Think of indices like page numbers in a book - they're always numbers, never words. If you want to access items by name/label, use a dictionary instead of a list!",
        'severity': 'error'
    },

    'bad-option-value': {
        'title': "⚙️ Invalid Configuration",
        'explain': "You're using an invalid value for a configuration option.",
        'how_to_fix': "Check the documentation for valid configuration values.",
        'wrong': "# pylint: disable=all  # Too broad!",
        'right': "# pylint: disable=C0103  # Specific rule",
        'learn': "💡 Be specific with configuration to maintain code quality!",
        'severity': 'error'
    },

    'inherit-non-class': {
        'title': "🚨 Inheriting from Non-Class",
        'explain': "You're trying to inherit from something that isn't a class.",
        'how_to_fix': "Make sure you're inheriting from an actual class object.",
        'wrong': "def my_function():\n    pass\n\nclass MyClass(my_function):  # Can't inherit from function!",
        'right': "class BaseClass:\n    pass\n\nclass MyClass(BaseClass):  # Inherit from class",
        'learn': "💡 Only classes can be used as base classes in inheritance!",
        'severity': 'error'
    },

    'inconsistent-mro': {
        'title': "🚨 Method Resolution Order Problem",
        'explain': "Python can't determine the order to call parent class methods. This happens with complex multiple inheritance.",
        'how_to_fix': "Reorganize your class inheritance to have a clear hierarchy.",
        'wrong': "class A(B, C): pass\nclass B(C): pass\nclass C(B): pass  # Circular!",
        'right': "class Base: pass\nclass A(Base): pass\nclass B(A): pass  # Clear hierarchy",
        'learn': "💡 Keep inheritance hierarchies simple - prefer composition over complex inheritance!",
        'severity': 'error'
    },

    'bad-super-call': {
        'title': "🚨 Incorrect super() Usage",
        'explain': "You're calling super() incorrectly or in the wrong context.",
        'how_to_fix': "Use super() only in methods, with correct arguments in Python 2 or no arguments in Python 3.",
        'wrong': "class Child(Parent):\n    def __init__(self):\n        super(WrongClass, self).__init__()  # Wrong class!",
        'right': "class Child(Parent):\n    def __init__(self):\n        super().__init__()  # Correct!",
        'learn': "💡 In Python 3, super() with no arguments is almost always what you want!",
        'severity': 'error'
    },

    'unhashable-dict-key': {
        'title': "🚨 Unhashable Dictionary Key",
        'explain': "You're trying to use a mutable object (like a list or dict) as a dictionary key, but only immutable objects can be keys.",
        'how_to_fix': "Use immutable objects (strings, numbers, tuples) as dictionary keys.",
        'wrong': "my_dict = {[1, 2]: 'value'}  # Lists can't be keys!",
        'right': "my_dict = {(1, 2): 'value'}  # Tuples can be keys!\n# OR\nmy_dict = {'1,2': 'value'}  # Strings work too",
        'learn': "💡 Dictionary keys must be hashable (immutable). Use tuples instead of lists, or convert to strings!",
        'severity': 'error'
    },

    'await-outside-async': {
        'title': "🚨 await Outside async Function",
        'explain': "You're using 'await' outside of an async function. await can only be used inside async def functions.",
        'how_to_fix': "Move the await into an async function, or use asyncio.run() at the top level.",
        'wrong': "result = await some_async_function()  # Not in async function!",
        'right': "async def main():\n    result = await some_async_function()  # Inside async!",
        'learn': "💡 'await' is the async equivalent of waiting for a function to finish - it needs async context!",
        'severity': 'error'
    },

    'bad-string-format-type': {
        'title': "🚨 Wrong Type in Format String",
        'explain': "You're using the wrong type specifier in a format string (like %d for a string).",
        'how_to_fix': "Match the format specifier to the variable type: %s for strings, %d for integers, %f for floats.",
        'wrong': "name = 'Alice'\nprint('Hello %d' % name)  # %d is for numbers!",
        'right': "name = 'Alice'\nprint('Hello %s' % name)  # %s for strings\n# OR better:\nprint(f'Hello {name}')  # f-strings!",
        'learn': "💡 Format specifiers: %s=string, %d=integer, %f=float. But f-strings are modern and easier!",
        'severity': 'error'
    },

    'return-arg-in-generator': {
        'title': "🚨 Return with Value in Generator",
        'explain': "You're using 'return value' inside a generator function. Generators should use 'yield', not 'return value'.",
        'how_to_fix': "Use 'yield' to return values from generators, or just 'return' (without a value) to stop.",
        'wrong': "def my_generator():\n    yield 1\n    return 42  # Can't return values!",
        'right': "def my_generator():\n    yield 1\n    yield 42  # Use yield\n    return  # Or just return (no value)",
        'learn': "💡 Generators use 'yield' to produce values. 'return' just stops the generator!",
        'severity': 'error'
    },

    'nonlocal-and-global': {
        'title': "🚨 Both nonlocal and global Used",
        'explain': "You can't use both 'nonlocal' and 'global' for the same variable in the same scope.",
        'how_to_fix': "Use either nonlocal (for outer function scope) or global (for module scope), not both.",
        'wrong': "def outer():\n    x = 1\n    def inner():\n        nonlocal x\n        global x  # Can't do both!",
        'right': "def outer():\n    x = 1\n    def inner():\n        nonlocal x  # For outer function scope",
        'learn': "💡 nonlocal = parent function, global = module level. Pick one!",
        'severity': 'error'
    },

    'invalid-context-manager': {
        'title': "🚨 Invalid Context Manager",
        'explain': "You're using 'with' on an object that doesn't support it. The object needs __enter__ and __exit__ methods.",
        'how_to_fix': "Only use 'with' on context managers (files, locks, etc.) or create your own with __enter__/__exit__.",
        'wrong': "with 42:  # Numbers aren't context managers!",
        'right': "with open('file.txt') as f:  # Files are context managers\n    data = f.read()",
        'learn': "💡 'with' is for automatic setup/cleanup. Files, locks, and database connections support it!",
        'severity': 'error'
    },

    'not-async-context-manager': {
        'title': "🚨 Not an Async Context Manager",
        'explain': "You're using 'async with' on an object that doesn't support it. It needs __aenter__ and __aexit__ methods.",
        'how_to_fix': "Only use 'async with' on async context managers, or use regular 'with' for sync objects.",
        'wrong': "async with open('file.txt') as f:  # open() is sync, not async!",
        'right': "# For async files:\nimport aiofiles\nasync with aiofiles.open('file.txt') as f:\n    data = await f.read()",
        'learn': "💡 'async with' needs async context managers. Regular files need regular 'with'!",
        'severity': 'error'
    },

    'yield-inside-async-function': {
        'title': "🚨 yield in Async Function",
        'explain': "You're using 'yield' in an async function. Use 'async def' with 'yield' to create an async generator.",
        'how_to_fix': "Make sure your function is defined as 'async def' if using yield in async context.",
        'wrong': "async def my_func():\n    yield 1  # Needs special handling",
        'right': "async def my_async_gen():  # Async generator\n    yield 1\n    yield 2",
        'learn': "💡 Async generators use 'async def' with 'yield' - they're for streaming async data!",
        'severity': 'error'
    },
    
    # ============================================
    # WARNINGS (Should Fix)
    # ============================================
    
    'unused-variable': {
        'title': "⚠️ Unused Variable Warning",
        'explain': "You created the variable '{symbol}' and assigned it a value, but then never used it anywhere in your code. This isn't an error (your code will run), but it's wasteful and confusing. It's like buying groceries and leaving them in the bag - why buy them if you're not going to use them? Unused variables make your code harder to read because people will wonder why they're there.",
        'how_to_fix': "Choose one of these solutions:\n1. Use the variable in your code (print it, pass it to a function, etc.)\n2. Remove the variable assignment entirely if you don't need it\n3. If you need it for later, add a comment explaining why\n4. If intentionally unused (for unpacking), prefix with underscore: _{symbol}",
        'wrong': "name = 'Alice'\nage = 25\nprint(name)  # age is created but never used!",
        'right': "name = 'Alice'\nage = 25\nprint(name, age)  # Now both are used!\n# OR just remove unused variable:\nname = 'Alice'\nprint(name)",
        'learn': "💡 Clean code has no waste! Every variable should have a purpose. Unused variables take up memory, slow down code reading, and might indicate unfinished logic. Think of your code like a recipe - don't include ingredients you won't use!",
        'severity': 'warning'
    },
    
    'unused-import': {
        'title': "⚠️ Unused Import Warning",
        'explain': "You imported the module '{symbol}' at the top of your file, but never actually used anything from it in your code. This is wasteful because Python loads the entire module into memory at startup, slowing down your program's launch time for no reason. It's like opening all your apps at once when you only need one - everything runs slower! This also clutters your code and confuses readers.",
        'how_to_fix': "Clean up your imports:\n1. Remove the import statement if you're not using the module\n2. If you plan to use it later, add a comment explaining why it's there\n3. Only import what you actually need (import specific items instead of the whole module)\n4. Keep imports organized (built-ins first, then third-party, then your own)",
        'wrong': "import math\nimport os\nimport sys\n\nprint(math.pi)  # Only math is used - os and sys are wasted!",
        'right': "import math\n\nprint(math.pi)  # Only import what you actually use!",
        'learn': "💡 Every import you add makes your program start slower! Keep imports lean and clean. It's like packing for a trip - only bring what you'll actually use. Unused imports are dead weight that slow you down!",
        'severity': 'warning'
    },
    
    'redefined-outer-name': {
        'title': "⚠️ Variable Shadows Outer Scope",
        'explain': "You have a variable named '{symbol}' in an outer scope (like global or in a parent function), and you're creating another variable with the same name '{symbol}' in an inner scope (like inside a function). This is called 'shadowing' - the inner variable hides the outer one, making the outer one unreachable. This causes confusing bugs because you might think you're using one variable but you're actually using a different one! It's like having two people with the same name in a room - very confusing!",
        'how_to_fix': "Use different, descriptive names:\n1. Give the inner variable a more specific name that describes its purpose\n2. Add a prefix or suffix to distinguish it (like user_name vs greeting_name)\n3. Think about whether you really need both variables\n4. Consider passing the outer variable as a parameter instead",
        'wrong': "name = 'Alice'  # Outer variable\n\ndef greet():\n    name = 'Bob'  # Shadows outer 'name' - confusing!\n    print(name)  # Prints Bob, not Alice",
        'right': "name = 'Alice'  # Original variable\n\ndef greet():\n    greeting_name = 'Bob'  # Clear, different name\n    print(greeting_name)\n    print(name)  # Can still access original",
        'learn': "💡 Variable shadowing is like having twins with identical names - it gets confusing fast! Use clear, distinct names for each variable. Good naming prevents bugs and makes code easier to understand. When in doubt, be more specific!",
        'severity': 'warning'
    },
    
    'redefined-builtin': {
        'title': "⚠️ Shadows Python Built-in Function",
        'explain': "You're using '{symbol}' as a variable name, but '{symbol}' is actually a built-in Python function! By using it as a variable, you've broken the original function - now you can't use it anywhere in your code. This is a serious problem because built-ins like list(), dict(), str(), and input() are essential Python features. It's like painting over a light switch - you've made something important unusable! This causes mysterious bugs later.",
        'how_to_fix': "Rename your variable to something else:\n1. Use a more descriptive name (items instead of list, data instead of dict)\n2. Add a suffix like _var or _data (list_data instead of list)\n3. Check common built-in names to avoid: list, dict, str, int, float, type, id, input, len, range, sum, max, min\n4. If you accidentally broke a built-in, restart your Python session to fix it",
        'wrong': "list = [1, 2, 3]  # Breaks list()!\ndict = {'a': 1}  # Breaks dict()!\nstr = 'hello'  # Breaks str()!\n\n# Now you can't use built-in functions!\n# list([1,2,3]) would fail!",
        'right': "items = [1, 2, 3]  # Good name\ndata = {'a': 1}  # Good name\ntext = 'hello'  # Good name\n\n# Built-ins still work!\nnew_list = list(range(5))",
        'learn': "💡 Python's built-in functions are precious tools - never cover them up! Think of built-ins like keys to your house - if you lose them (by shadowing), you're locked out! Memorize common built-ins to avoid: list, dict, str, int, type, id, input, len, max, min, sum. When naming variables, be creative and descriptive!",
        'severity': 'warning'
    },
    
    'eval-used': {
        'title': "⚠️ Dangerous eval() Usage",
        'explain': "Using eval() is dangerous as it can execute arbitrary code!",
        'how_to_fix': "Use safer alternatives like ast.literal_eval() or json.loads().",
        'wrong': "user_input = input('Enter expression: ')\nresult = eval(user_input)  # Dangerous!",
        'right': "import ast\nuser_input = input('Enter value: ')\nresult = ast.literal_eval(user_input)  # Safe!",
        'learn': "💡 eval() can execute any Python code, including malicious code. Never use it with user input!",
        'severity': 'warning'
    },
    
    'exec-used': {
        'title': "⚠️ Dangerous exec() Usage",
        'explain': "Using exec() can execute any Python code, which is a major security risk!",
        'how_to_fix': "Redesign your code to avoid dynamic code execution.",
        'wrong': "code = input('Enter code: ')\nexec(code)  # Very dangerous!",
        'right': "# Don't use exec with user input!\n# Redesign to use functions/data structures instead",
        'learn': "💡 exec() is almost never needed. If you think you need it, there's usually a better way!",
        'severity': 'warning'
    },
    
    'dangerous-default-value': {
        'title': "⚠️ Dangerous Mutable Default Argument",
        'explain': "You're using a mutable object (list [] or dict {}) as a default argument in your function. This is one of Python's most famous 'gotchas'! The problem: default arguments are created ONCE when the function is defined, not each time it's called. So all function calls share the same list/dict object! This causes bizarre bugs where data from previous calls mysteriously appears. It's like everyone in a restaurant sharing one plate - whatever the previous person added stays there!",
        'how_to_fix': "Use None as default, create the mutable inside:\n1. Change the default from =[] to =None\n2. Inside the function, add: if parameter is None: parameter = []\n3. Now each call gets its own fresh list/dict\n4. This pattern is so common it's the 'Pythonic' way to do it",
        'wrong': "def add_item(item, items=[]):  # DANGEROUS!\n    items.append(item)\n    return items\n\nadd_item('apple')  # ['apple']\nadd_item('banana')  # ['apple', 'banana'] - Wait, what!?",
        'right': "def add_item(item, items=None):  # Safe!\n    if items is None:\n        items = []  # Fresh list each time\n    items.append(item)\n    return items\n\nadd_item('apple')  # ['apple']\nadd_item('banana')  # ['banana'] - Correct!",
        'learn': "💡 Default arguments are created at function definition time (once), not at call time (every time). Think of it like a template that's filled in once and reused forever. Mutable defaults are like a communal whiteboard - everyone adds to it and nothing gets erased! Always use None for mutable defaults - it's a Python best practice!",
        'severity': 'warning'
    },
    
    'global-statement': {
        'title': "⚠️ Global Variable Usage",
        'explain': "Using global variables makes code harder to understand and test.",
        'how_to_fix': "Pass values as parameters and return results instead.",
        'wrong': "counter = 0\n\ndef increment():\n    global counter\n    counter += 1",
        'right': "def increment(counter):\n    return counter + 1\n\ncounter = 0\ncounter = increment(counter)",
        'learn': "💡 Functions should be like vending machines: you put something in (parameters), get something out (return value)!",
        'severity': 'warning'
    },
    
    'consider-using-with': {
        'title': "⚠️ Resource Not Using Context Manager",
        'explain': "Files and other resources should use 'with' statement to ensure proper cleanup.",
        'how_to_fix': "Use 'with' statement when opening files.",
        'wrong': "f = open('file.txt')\ndata = f.read()\nf.close()  # Might not run if error occurs!",
        'right': "with open('file.txt') as f:\n    data = f.read()  # Auto-closed!",
        'learn': "💡 'with' guarantees cleanup even if errors occur. It's like an automatic door!",
        'severity': 'warning'
    },
    
    'bare-except': {
        'title': "⚠️ Bare Except Clause",
        'explain': "Bare 'except:' catches ALL exceptions, including system exits!",
        'how_to_fix': "Specify which exceptions to catch.",
        'wrong': "try:\n    risky_operation()\nexcept:  # Catches everything!\n    pass",
        'right': "try:\n    risky_operation()\nexcept ValueError:  # Specific exception\n    pass",
        'learn': "💡 Only catch exceptions you know how to handle!",
        'severity': 'warning'
    },
    
    'unidiomatic-typecheck': {
        'title': "⚠️ Use isinstance() for Type Checking",
        'explain': "Using type() for type checking is not Pythonic and doesn't work with inheritance.",
        'how_to_fix': "Use isinstance() instead.",
        'wrong': "if type(value) == list:\n    process(value)",
        'right': "if isinstance(value, list):\n    process(value)",
        'learn': "💡 isinstance() respects inheritance and is the Pythonic way!",
        'severity': 'warning'
    },
    
    'broad-exception-caught': {
        'title': "⚠️ Overly Broad Exception",
        'explain': "Catching Exception is too broad - it catches almost everything!",
        'how_to_fix': "Catch specific exceptions you expect.",
        'wrong': "try:\n    value = int(input())\nexcept Exception:  # Too broad!\n    print('Error')",
        'right': "try:\n    value = int(input())\nexcept ValueError:  # Specific!\n    print('Please enter a number')",
        'learn': "💡 Catch only the exceptions you expect and know how to handle!",
        'severity': 'warning'
    },
    
    'attribute-defined-outside-init': {
        'title': "⚠️ Attribute Not in __init__",
        'explain': "Class attributes should be defined in __init__ for clarity.",
        'how_to_fix': "Move attribute definition to __init__ method.",
        'wrong': "class Person:\n    def __init__(self, name):\n        self.name = name\n    \n    def set_age(self, age):\n        self.age = age  # Defined here!",
        'right': "class Person:\n    def __init__(self, name):\n        self.name = name\n        self.age = None  # Defined in __init__",
        'learn': "💡 Defining attributes in __init__ makes it clear what attributes an object has!",
        'severity': 'warning'
    },
    
    'protected-access': {
        'title': "⚠️ Accessing Protected Member",
        'explain': "Accessing '{symbol}' (starts with _) breaks encapsulation.",
        'how_to_fix': "Use public methods to access the data, or make the attribute public if needed.",
        'wrong': "user._password  # Accessing protected attribute!",
        'right': "user.get_password()  # Use public method",
        'learn': "💡 Names starting with _ are meant to be internal. Respect the privacy!",
        'severity': 'warning'
    },
    
    'unreachable': {
        'title': "⚠️ Unreachable Code",
        'explain': "This code will never be executed because it comes after a return, break, or raise statement.",
        'how_to_fix': "Remove the unreachable code or fix the control flow.",
        'wrong': "def calculate():\n    return 42\n    print('done')  # Never runs!",
        'right': "def calculate():\n    print('done')  # Runs first\n    return 42",
        'learn': "💡 Code after return/break/raise is dead code - it never executes!",
        'severity': 'warning'
    },
    
    'pointless-statement': {
        'title': "⚠️ Statement Has No Effect",
        'explain': "You wrote a statement that calculates something or evaluates an expression, but then you do nothing with the result! Python calculates it and immediately throws it away. This is almost always a mistake - either you forgot to assign it to a variable, or you accidentally left some debug code, or you're thinking of another language where statements have side effects. It's like cooking a meal and throwing it in the trash without eating it!",
        'how_to_fix': "Fix based on what you intended:\n1. Store the result: x = x + 5 or result = calculate()\n2. If calling a function for side effects: make sure it actually does something\n3. Remove the line if it's leftover debug/test code\n4. Add an operation: print(expression) or append(expression)",
        'wrong': "x + 5  # Calculated and immediately discarded!\nmy_list.sort  # Forgot to call it with ()\n'hello'.upper()  # Calculated but not used\n\nx = 10\nx * 2  # Calculated but x doesn't change!",
        'right': "x = x + 5  # Store the result\nmy_list.sort()  # Actually call it\ngreeting = 'hello'.upper()  # Store result\n\nx = 10\nx = x * 2  # Actually update x",
        'learn': "💡 Every statement should DO something! In Python, calculations don't change anything unless you assign them or pass them somewhere. This is different from languages where operations might have hidden side effects. If you're calculating something, you probably want to store it, print it, return it, or pass it to a function. A statement that does nothing is usually a typo or incomplete thought!",
        'severity': 'warning'
    },
    
    'unused-argument': {
        'title': "⚠️ Unused Function Parameter",
        'explain': "Your function defines a parameter '{symbol}' but never uses it anywhere in the function body. This usually means: 1) You forgot to use it (incomplete function), 2) The requirements changed but you didn't remove it, or 3) It's required by an interface/API but your implementation doesn't need it. Unused parameters are confusing because callers think they matter, but they don't! It's like a recipe that lists salt as an ingredient but never tells you to add it.",
        'how_to_fix': "Choose based on the situation:\n1. Use the parameter if you forgot to: use '{symbol}' in your function logic\n2. Remove it if not needed: delete '{symbol}' from parameters\n3. For required interfaces: prefix with underscore: _{symbol}\n4. For callbacks with fixed signatures: use *args or **kwargs for unused parts",
        'wrong': "def greet(name, age, city):\n    print(f'Hello {name}')  # age and city never used!\n\ndef calculate_discount(price, customer_type, membership_level):\n    return price * 0.9  # Ignoring customer_type and membership!",
        'right': "# Use all parameters:\ndef greet(name, age, city):\n    print(f'Hello {name}, {age} years old from {city}')\n\n# OR remove unused ones:\ndef greet(name):\n    print(f'Hello {name}')\n\n# OR prefix if required by interface:\ndef callback(event, _context):\n    process(event)  # _context shows it's intentionally unused",
        'learn': "💡 Function parameters are a contract - they tell callers what information the function needs. Unused parameters break this contract by implying something is needed when it isn't. This wastes the caller's effort gathering that data! Clean, professional code has no unused parameters. Prefix with _ only for cases where an interface forces you to accept parameters you don't need (like callback APIs).",
        'severity': 'warning'
    },
    
    'wildcard-import': {
        'title': "⚠️ Wildcard Import - Import Everything",
        'explain': "You're using 'from module import *' which imports EVERYTHING from that module into your namespace. This is dangerous and considered bad practice because: 1) It can silently overwrite your existing variables/functions with the same names, 2) It makes code unreadable (where did this function come from?), 3) It imports things you don't need, wasting memory, 4) Tools like linters and IDEs can't help you because they don't know what '*' imported. It's like dumping an entire toolbox on your desk when you only need a screwdriver!",
        'how_to_fix': "Import only what you need:\n1. Replace: from math import *\n2. With: from math import pi, sqrt, cos (list specific items)\n3. Or import the module: import math, then use math.pi\n4. Check what you're actually using from the module\n5. For exploratory coding, import module first, then make explicit later",
        'wrong': "from math import *  # Imports ~50 functions/constants!\nfrom os import *  # Imports 150+ items!\n\n# Now you have no idea where functions come from:\nresult = sqrt(25)  # Is this math.sqrt or from somewhere else?\npath = getcwd()  # Where did getcwd come from?",
        'right': "# Explicit imports - crystal clear:\nfrom math import sqrt, pi, cos\nfrom os import getcwd, listdir\n\nresult = sqrt(25)  # Obviously from math\npath = getcwd()  # Obviously from os\n\n# OR import the module:\nimport math\nimport os\n\nresult = math.sqrt(25)\npath = os.getcwd()",
        'learn': "💡 Explicit is better than implicit - a core Python principle! Wildcard imports are like turning on every light in your house when you need one room. They clutter your namespace, hide the origin of functions, and can cause mysterious bugs when names collide. Professional Python code NEVER uses wildcard imports (except in very specific interactive scenarios). Be explicit, be clear, help future readers (including yourself)!",
        'severity': 'warning'
    },
    
    'reimported': {
        'title': "⚠️ Module Reimported",
        'explain': "You're importing the same module multiple times.",
        'how_to_fix': "Remove duplicate imports.",
        'wrong': "import os\nimport sys\nimport os  # Already imported!",
        'right': "import os\nimport sys  # Import once",
        'learn': "💡 Each module only needs to be imported once!",
        'severity': 'warning'
    },
    
    'using-constant-test': {
        'title': "⚠️ Using Constant in Conditional",
        'explain': "Your if/while condition uses a constant value (True, False, or a literal number/string) that never changes. This means the condition's outcome is already known before the program runs! If it's 'if True:', the code always runs. If it's 'if False:', it never runs. Why have a condition that never actually tests anything? It's like a door that's always open or always locked - not much of a door! This is usually debug/test code left by mistake.",
        'how_to_fix': "Fix based on intent:\n1. If always true: Remove the if statement, just run the code directly\n2. If always false: Remove the entire if block (dead code)\n3. If temporary testing: Replace constant with actual variable/condition\n4. For while True: This is okay for infinite loops (but add break conditions)",
        'wrong': "if True:  # Always runs - why have the if?\n    process_data()\n\nif False:  # Never runs - dead code!\n    important_function()\n\nwhile 1:  # Infinite loop without break\n    do_something()",
        'right': "# Just run it directly:\nprocess_data()  # No pointless if needed\n\n# If testing, use actual condition:\nif should_process:\n    process_data()\n\n# While True is OK for infinite loops:\nwhile True:  # Intentional infinite loop\n    if exit_condition:\n        break  # But add exit!",
        'learn': "💡 Conditions exist to make decisions at runtime! A constant condition is a decision that's already made at coding time, so why pretend to decide? The only exception: 'while True:' for intentional infinite loops (server loops, game loops), but even then you need break conditions. If you're using constants for testing, use actual test frameworks instead. Dead code (if False) should be deleted, not left commented out by conditions!",
        'severity': 'warning'
    },
    
    'duplicate-key': {
        'title': "⚠️ Duplicate Dictionary Key",
        'explain': "You have the same key appearing multiple times in a single dictionary definition. Python doesn't error on this, but it silently keeps only the LAST value - all previous values for that key are lost! This is almost always a mistake: either you have a typo, meant to use different keys, or didn't realize you already used that key. It's like labeling two different boxes with the same name - you'll only find what you put in the last one!",
        'how_to_fix': "Fix the duplicate keys:\n1. Check for typos in key names\n2. Use unique, descriptive keys: 'first_name' vs 'last_name' instead of 'name' twice\n3. If the data truly belongs to the same key, use a list or nested dict\n4. Review your data structure - maybe you need a different organization",
        'wrong': "# Duplicate key 'name' - only Bob survives!\nuser = {\n    'name': 'Alice',\n    'age': 25,\n    'name': 'Bob'  # Overwrites Alice!\n}\nprint(user['name'])  # Prints 'Bob', Alice is lost\n\nconfig = {\n    'host': 'localhost',\n    'port': 8000,\n    'host': '127.0.0.1'  # Overwrites localhost\n}",
        'right': "# Use unique keys:\nuser = {\n    'first_name': 'Alice',\n    'age': 25,\n    'last_name': 'Bob'\n}\n\n# OR if multiple values for same concept:\nconfig = {\n    'hosts': ['localhost', '127.0.0.1'],  # List of hosts\n    'port': 8000\n}\n\n# OR separate dicts:\nprimary = {'host': 'localhost'}\nfallback = {'host': '127.0.0.1'}",
        'learn': "💡 Dictionary keys must be unique within a dictionary - that's the whole point of dictionaries! They're key-value mappings where each key points to ONE value. Duplicates are Python's silent killers - no error, just data loss. Always use distinct keys. If you need multiple values for similar things, use lists, nested dicts, or separate dictionaries. This mistake often reveals poor data modeling!",
        'severity': 'warning'
    },
    
    'unnecessary-lambda': {
        'title': "⚠️ Unnecessary Lambda Function",
        'explain': "You're using a lambda that just passes its arguments directly to another function without any transformation. This is redundant - you can pass the function itself directly! Lambda should only be used when you need to do something WITH the arguments (transform, combine, etc.), not when you're just forwarding them unchanged. It's like hiring a middleman who just repeats what you say word-for-word - why have the middleman?",
        'how_to_fix': "Remove the lambda wrapper:\n1. Replace: lambda x: func(x) with just: func\n2. The function name IS already a reference you can pass\n3. Only keep lambda if you're actually transforming: lambda x: func(x) + 1\n4. Functions are first-class objects in Python - you can pass them around!",
        'wrong': "numbers = ['5', '2', '10', '1']\nnumbers.sort(key=lambda x: int(x))  # Unnecessary!\n\nnames = ['alice', 'bob', 'charlie']\nnames.sort(key=lambda x: x.upper())  # Unnecessary!\n\nitems = map(lambda x: str(x), numbers)  # Unnecessary!",
        'right': "numbers = ['5', '2', '10', '1']\nnumbers.sort(key=int)  # Direct reference!\n\nnames = ['alice', 'bob', 'charlie']\nnames.sort(key=str.upper)  # Direct method reference!\n\nitems = map(str, numbers)  # Direct reference!\n\n# Lambda IS needed when transforming:\nnumbers.sort(key=lambda x: -int(x))  # Reverse order\nnames.sort(key=lambda x: len(x))  # Sort by length",
        'learn': "💡 Lambda is for small, anonymous functions that transform data. If you're just passing arguments through unchanged, you don't need lambda - the function name itself is a reference you can pass! This is cleaner, faster, and more readable. Think of functions like tools: you can hand someone a tool directly, you don't need to hand them a box that contains the tool. Only use lambda when you need to do something extra!",
        'severity': 'warning'
    },
    
    'assert-on-tuple': {
        'title': "⚠️ Assert on Tuple (Always True)",
        'explain': "Asserting on a tuple is always True (even empty tuples are truthy)!",
        'how_to_fix': "Use proper assertion syntax.",
        'wrong': "assert (x > 0, 'x must be positive')  # Wrong! Always True",
        'right': "assert x > 0, 'x must be positive'  # Correct syntax",
        'learn': "💡 Watch the parentheses in assertions - they change the meaning!",
        'severity': 'warning'
    },
    
    'unbalanced-tuple-unpacking': {
        'title': "⚠️ Unbalanced Tuple Unpacking",
        'explain': "You're trying to unpack a sequence (tuple/list) into variables, but the number of variables doesn't match the number of values! Python doesn't know what to do with the extra values or how to fill the missing variables. This is like trying to put 3 items into 2 boxes or 2 items into 3 boxes - it doesn't work! Common causes: 1) Function returns changed, 2) You miscounted, 3) The sequence is dynamic and you assumed wrong size.",
        'how_to_fix': "Match the counts:\n1. Count both sides: a, b, c = (1, 2, 3) - three and three!\n2. Use * for 'rest': a, b, *rest = (1, 2, 3, 4) - rest gets [3, 4]\n3. Use _ for unwanted values: a, _, c = (1, 2, 3) - ignores middle\n4. Check function return if unpacking a function call\n5. Add variables or adjust the sequence",
        'wrong': "# Too few variables:\na, b = (1, 2, 3)  # ValueError: too many values to unpack!\n\n# Too many variables:\na, b, c = (1, 2)  # ValueError: not enough values!\n\n# From function:\ndef get_data():\n    return 1, 2, 3  # Returns 3 items\n    \nx, y = get_data()  # Error: trying to unpack 3 into 2!",
        'right': "# Match the counts:\na, b, c = (1, 2, 3)  # Perfect match!\n\n# Use * for remainder:\na, b, *rest = (1, 2, 3, 4, 5)  # rest gets [3, 4, 5]\n\n# Ignore with _:\na, _, c = (1, 2, 3)  # _ captures 2 (convention for 'don't care')\n\n# Correct function unpacking:\ndef get_data():\n    return 1, 2, 3\n    \nx, y, z = get_data()  # All 3 captured!\n\n# Or use *:\nfirst, *others = get_data()  # first=1, others=[2,3]",
        'learn': "💡 Unpacking is Python's way of saying 'split this sequence into separate variables'. The counts must match exactly, unless you use * to capture multiple items. Think of it like dealing cards - if you have 3 cards but only 2 hands, someone's not getting a full hand! The * operator is powerful: it captures 'everything else' into a list. Use _ by convention when you don't care about a value.",
        'severity': 'warning'
    },
    
    'unpacking-non-sequence': {
        'title': "⚠️ Trying to Unpack Non-Sequence",
        'explain': "You're trying to unpack (split into multiple variables) something that isn't a sequence. Only sequences (lists, tuples, strings) and iterables can be unpacked. You can't unpack single values like numbers, booleans, or None. This usually means: 1) You thought a function returned a tuple but it returns a single value, 2) You're trying to unpack None (function returned nothing), or 3) Logical error in what you expect the data to be. It's like trying to split a single coin into two coins - it's already atomic!",
        'how_to_fix': "Check what you're unpacking:\n1. Verify the value is actually a sequence: print(type(value))\n2. If it's a single value, don't unpack: x = get_value() not x, y = get_value()\n3. If function returns None: fix the function to return a tuple\n4. If sometimes single, sometimes tuple: handle both cases\n5. Wrap single values in a tuple if you want to unpack: (value,)",
        'wrong': "# Unpacking non-sequences:\na, b = 42  # TypeError: int is not iterable\nx, y = None  # TypeError: NoneType is not iterable\n\ndef get_value():\n    return 5  # Returns single int\n    \nfirst, second = get_value()  # Error: can't unpack int!\n\n# Function returned None:\ndef process():\n    print('done')  # No return = returns None\n    \nresult, status = process()  # Error: can't unpack None!",
        'right': "# Unpack sequences:\na, b = (4, 2)  # Tuple: OK\nx, y = [10, 20]  # List: OK\nf, l = 'Hi'  # String: OK (f='H', l='i')\n\ndef get_value():\n    return 5  # Single value\n    \nvalue = get_value()  # Don't unpack, just assign\n\n# If function should return tuple:\ndef get_values():\n    return 5, 10  # Returns tuple\n    \nfirst, second = get_values()  # Works!\n\n# Handle both cases:\nresult = get_data()  # Get it first\nif isinstance(result, tuple):\n    x, y = result  # Unpack if tuple\nelse:\n    x = result  # Use directly if not",
        'learn': "💡 Unpacking is only for 'splittable' things - sequences that contain multiple items. A single number, boolean, or None can't be split because they're atomic (single units). Think of unpacking like opening a box to take out multiple items - you need a box with multiple items! If a function might return different types (sometimes tuple, sometimes single value), that's usually poor design. Be consistent: either always return a tuple or always return a single value.",
        'severity': 'warning'
    },

    'comparison-with-callable': {
        'title': "⚠️ Comparing Function Without Calling It",
        'explain': "You're comparing a function or method directly in a condition, but you forgot to call it with parentheses ()! Without parentheses, you're comparing the function object itself, not its return value. The function object is always truthy, so 'if my_function:' is always True, and 'if my_function == True' is always False (comparing function object to True). This is a very common beginner mistake - it's like checking if a phone exists instead of actually making the call!",
        'how_to_fix': "Add parentheses to call the function:\n1. Change: if my_function → if my_function()\n2. Change: if func == True → if func() == True (or just if func())\n3. If you actually want to check if function exists: if my_function is not None\n4. Remember: functions need () to execute!",
        'wrong': "def is_valid():\n    return True\n\n# Forgot to call it!\nif is_valid:  # Always True (function exists)\n    print('Valid')\n\nif is_valid == True:  # Always False (function object != True)\n    print('Never prints')\n\n# More examples:\nresult = calculate  # Assigns function, doesn't call it\nwhile should_continue:  # Forgot (), infinite loop!",
        'right': "def is_valid():\n    return True\n\n# Call it with ():\nif is_valid():  # Actually calls and checks return value\n    print('Valid')\n\n# Correct usage:\nresult = calculate()  # Calls function\nwhile should_continue():  # Calls and checks each time\n\n# If checking if function exists:\nif is_valid is not None:\n    result = is_valid()  # Then call it",
        'learn': "💡 Functions are objects in Python! Without (), you're working with the function object itself (the machine), not running it (the result). This is like holding a calculator instead of pressing the buttons. When used in conditions, function objects are always 'truthy' regardless of what they would return. Always add () to call functions. The only time you don't use () is when passing functions as arguments (like in callbacks).",
        'severity': 'warning'
    },

    'arguments-renamed': {
        'title': "⚠️ Arguments Renamed in Override",
        'explain': "When overriding a parent class method, you changed the parameter names. This can be confusing.",
        'how_to_fix': "Keep the same parameter names as the parent class method for clarity.",
        'wrong': "class Parent:\n    def process(self, data): pass\n\nclass Child(Parent):\n    def process(self, info):  # Different name!",
        'right': "class Parent:\n    def process(self, data): pass\n\nclass Child(Parent):\n    def process(self, data):  # Same name!",
        'learn': "💡 Consistent parameter names make inheritance easier to understand!",
        'severity': 'warning'
    },

    'unused-private-member': {
        'title': "⚠️ Unused Private Member",
        'explain': "You defined a private method/attribute (starting with _) but never use it.",
        'how_to_fix': "Either use the private member or remove it if unnecessary.",
        'wrong': "class MyClass:\n    def __init__(self):\n        self._helper = 42  # Never used!",
        'right': "class MyClass:\n    def __init__(self):\n        self._helper = 42\n    \n    def calculate(self):\n        return self._helper * 2  # Used!",
        'learn': "💡 Private members (starting with _) should be used internally in the class!",
        'severity': 'warning'
    },

    'format-needs-mapping': {
        'title': "⚠️ Format String Needs Mapping",
        'explain': "Your format string uses named placeholders %(name)s but you're passing a non-dict argument.",
        'how_to_fix': "Pass a dictionary when using named placeholders.",
        'wrong': "'Hello %(name)s' % 'Alice'  # Can't use string with %(name)s!",
        'right': "'Hello %(name)s' % {'name': 'Alice'}  # Pass a dict!",
        'learn': "💡 Named placeholders %(name)s need a dictionary. Positional %s takes direct values!",
        'severity': 'warning'
    },

    'dict-iter-missing-items': {
        'title': "⚠️ Dictionary Iteration Without .items()",
        'explain': "You're iterating over a dictionary but seem to want key-value pairs. Use .items()!",
        'how_to_fix': "Use .items() when you need both keys and values.",
        'wrong': "for key in my_dict:\n    print(key, my_dict[key])  # Extra lookup",
        'right': "for key, value in my_dict.items():\n    print(key, value)  # Clean!",
        'learn': "💡 .items() gives you both key and value without extra lookups!",
        'severity': 'warning'
    },

    'useless-parent-delegation': {
        'title': "💡 Useless Method Override",
        'explain': "Your method override just calls the parent method with the same arguments. This is pointless!",
        'how_to_fix': "Remove the method override if it doesn't add anything.",
        'wrong': "class Child(Parent):\n    def process(self, data):\n        return super().process(data)  # Does nothing extra!",
        'right': "class Child(Parent):\n    # Just remove the method - inherit parent's version\n    pass",
        'learn': "💡 Only override methods when you need to change behavior!",
        'severity': 'warning'
    },
    
   
    
    # ============================================
    # CONVENTIONS (Good Practices)
    # ============================================
    
    'invalid-name': {
        'title': "📏 Naming Convention Violation",
        'explain': "The name '{symbol}' doesn't follow Python's official naming conventions (PEP 8). Python has specific naming styles for different things, and using the right style makes your code instantly recognizable to other Python developers. It's like using the wrong punctuation in English - people can understand it, but it looks unprofessional and confusing. Consistent naming is one of the easiest ways to make your code look professional!",
        'how_to_fix': "Follow Python naming conventions:\n1. Variables & functions: snake_case (lowercase with underscores): user_name, calculate_total\n2. Classes: PascalCase (capitalize each word): UserProfile, DataProcessor\n3. Constants: UPPER_CASE (all caps with underscores): MAX_SIZE, API_KEY\n4. Avoid single letters except for loops (i, j) or coordinates (x, y)",
        'wrong': "MyVariable = 5  # Wrong - looks like a class!\nmy-variable = 5  # Wrong - invalid syntax!\nMYfunction = lambda: None  # Wrong - looks like a constant!\ncalculateTotal = 10  # Wrong - this is JavaScript style!",
        'right': "my_variable = 5  # Correct for variables\nMY_CONSTANT = 5  # Correct for constants\nclass MyClass:  # Correct for classes\n    pass\n\ndef calculate_total():  # Correct for functions\n    pass",
        'learn': "💡 Consistent naming is like a universal language among Python developers! When everyone follows the same rules, code becomes instantly readable. Think of it like traffic signs - they work because everyone agrees on what they mean. snake_case for variables/functions, PascalCase for classes, UPPER_CASE for constants. Master these and your code will look professional!",
        'severity': 'convention'
    },
    
    'line-too-long': {
        'title': "📏 Line Length Exceeds Limit",
        'explain': "This line is longer than the recommended 79-100 characters. Python's style guide (PEP 8) suggests keeping lines short because: 1) Long lines are hard to read without scrolling, 2) They cause problems in side-by-side code reviews, 3) They don't fit well on smaller screens, 4) They often indicate the code is trying to do too much at once. It's like writing a run-on sentence - technically valid, but hard to follow!",
        'how_to_fix': "Break long lines into multiple lines:\n1. For function calls: Put each argument on its own line inside parentheses\n2. For strings: Use implicit string concatenation or triple quotes\n3. For conditions: Break before operators (and, or) and indent\n4. For lists/dicts: Put each item on a new line\n5. Most editors can show a line guide at 79 or 100 characters",
        'wrong': "result = some_function(argument1, argument2, argument3, argument4, argument5, argument6, argument7, argument8)  # Too long!\n\nmessage = 'This is a very long string that contains lots of information and goes on and on and on...'",
        'right': "# Multi-line function call:\nresult = some_function(\n    argument1, argument2, argument3,\n    argument4, argument5, argument6,\n    argument7, argument8\n)\n\n# Multi-line string:\nmessage = (\n    'This is a very long string that contains '\n    'lots of information and goes on and on...'\n)",
        'learn': "💡 Short lines are like short paragraphs - easier to read and understand! The 79-character limit comes from old terminals, but it's still useful today. Think of it as writing for readability, not just for the machine. If a line is too long, it's often a sign that you're doing too much in one place - consider breaking the logic into smaller pieces!",
        'severity': 'convention'
    },
    
    'consider-using-enumerate': {
        'title': "💡 Consider Using enumerate()",
        'explain': "You're using range(len()) to loop through a list and access items by index. This is a common pattern from other programming languages, but Python has a much better way: enumerate()! Your current approach is harder to read, more error-prone (wrong indices), and not 'Pythonic'. It's like using a butter knife to eat soup when you have a spoon right there - it works, but why make it harder?",
        'how_to_fix': "Replace range(len()) with enumerate():\n1. Change: for i in range(len(items))\n2. To: for i, item in enumerate(items)\n3. Now use 'item' directly instead of 'items[i]'\n4. You get both the index (i) and the value (item) automatically\n5. Optionally add start=1 if you want counting from 1: enumerate(items, start=1)",
        'wrong': "items = ['apple', 'banana', 'cherry']\nfor i in range(len(items)):\n    print(i, items[i])  # Clunky indexing\n\n# Easy to make mistakes:\nfor i in range(len(items)):\n    if items[i] == 'banana':  # What if index is wrong?",
        'right': "items = ['apple', 'banana', 'cherry']\nfor i, item in enumerate(items):\n    print(i, item)  # Clean and clear!\n\n# Much more readable:\nfor i, item in enumerate(items):\n    if item == 'banana':  # Direct access, no indexing errors!",
        'learn': "💡 enumerate() is Python's way of saying 'count and give'. Instead of manually tracking the count with range(len()), let Python do it for you! It's safer (no index errors), cleaner (no brackets), and more readable (clear intent). This is one of Python's superpowers - use it! Think of enumerate() as a helpful assistant who counts items for you while you work with them.",
        'severity': 'convention'
    },
    
    'consider-iterating-dictionary': {
        'title': "💡 Direct Dictionary Iteration",
        'explain': "You can iterate directly over dictionary items.",
        'how_to_fix': "Use .items() for cleaner iteration.",
        'wrong': "for key in my_dict.keys():\n    value = my_dict[key]",
        'right': "for key, value in my_dict.items():\n    print(key, value)",
        'learn': "💡 .items() gives you both key and value elegantly!",
        'severity': 'convention'
    },
    
    'missing-function-docstring': {
        'title': "📚 Missing Function Docstring",
        'explain': "Your function doesn't have a docstring (documentation string). Docstrings explain what a function does, what parameters it takes, and what it returns. Without docstrings, other developers (and future you!) have to read all the code to understand what it does. It's like having a tool with no label - you have to experiment to figure out what it's for! Even simple functions benefit from a one-line docstring.",
        'how_to_fix': "Add a docstring right after the function definition:\n1. Use triple quotes (\"\"\" or ''')\n2. Put it on the first line after def\n3. For simple functions: one line explaining what it does\n4. For complex functions: describe parameters, return value, and any side effects\n5. Use present tense: 'Calculate total' not 'Calculates total'",
        'wrong': "def calculate_total(items):\n    # No docstring!\n    return sum(items)\n\ndef process_data(data, option=None):\n    # Complex function with no documentation\n    if option == 'clean':\n        return [x.strip() for x in data]\n    return data",
        'right': 'def calculate_total(items):\n    """Calculate the sum of all items in the list."""\n    return sum(items)\n\ndef process_data(data, option=None):\n    """Process data based on the given option.\n    \n    Args:\n        data: List of strings to process\n        option: Processing mode (\'clean\' to strip whitespace)\n    \n    Returns:\n        Processed list of strings\n    """\n    if option == \'clean\':\n        return [x.strip() for x in data]\n    return data',
        'learn': "💡 Docstrings are love letters to your future self! When you come back to code after 6 months, you'll thank yourself for explaining what it does. Professional Python code always has docstrings - it's not optional! Think of docstrings as user manuals for your functions. The help() function and IDEs show docstrings, making your code self-documenting. Write them as you code, not later!",
        'severity': 'convention'
    },

    
    'unspecified-encoding': {
        'title': "📝 Specify File Encoding",
        'explain': "Always specify encoding when opening files to avoid platform issues.",
        'how_to_fix': "Add encoding='utf-8' to open() calls.",
        'wrong': "with open('file.txt') as f:\n    data = f.read()",
        'right': "with open('file.txt', encoding='utf-8') as f:\n    data = f.read()",
        'learn': "💡 UTF-8 is the standard. Explicit encoding prevents surprises on different systems!",
        'severity': 'convention'
    },
    
    'trailing-whitespace': {
        'title': "🧹 Trailing Whitespace",
        'explain': "There's unnecessary whitespace at the end of this line.",
        'how_to_fix': "Remove trailing spaces. Most editors can do this automatically.",
        'wrong': "name = 'Alice'    ",
        'right': "name = 'Alice'",
        'learn': "💡 Trailing whitespace causes git diffs and merge conflicts. Keep lines clean!",
        'severity': 'convention'
    },
    
    'multiple-statements': {
        'title': "📏 Multiple Statements on One Line",
        'explain': "Having multiple statements on one line reduces readability.",
        'how_to_fix': "Put each statement on its own line.",
        'wrong': "x = 5; y = 10; z = x + y",
        'right': "x = 5\ny = 10\nz = x + y",
        'learn': "💡 One statement per line makes code easier to read and debug!",
        'severity': 'convention'
    },
    
    'unnecessary-pass': {
        'title': "🎯 Unnecessary pass Statement",
        'explain': "You have a 'pass' statement in a block that already has other code. 'pass' is only needed as a placeholder for completely empty blocks - once you have actual statements, pass serves no purpose and just clutters the code. It's like putting a 'placeholder' sign in a room that's already full of furniture - the room clearly isn't empty! This often happens when you start with pass for an empty block, then add code but forget to remove pass.",
        'how_to_fix': "Remove the pass statement:\n1. If block has other statements: just delete the pass line\n2. Keep pass ONLY in completely empty blocks: if x: pass\n3. Empty blocks need something (pass or ...) or Python gives syntax error\n4. Review why the block is empty - maybe add a comment explaining why",
        'wrong': "if condition:\n    do_something()\n    pass  # Not needed - block has code!\n\ndef process():\n    print('Processing')\n    pass  # Not needed!\n\nfor item in items:\n    item.process()\n    pass  # Not needed!",
        'right': "if condition:\n    do_something()  # pass removed\n\ndef process():\n    print('Processing')  # pass removed\n\nfor item in items:\n    item.process()  # pass removed\n\n# pass IS needed for empty blocks:\nif condition:\n    pass  # Placeholder - will implement later\n\ndef placeholder():\n    pass  # Empty function stub\n\nclass EmptyClass:\n    pass  # Empty class definition",
        'learn': "💡 'pass' means 'do nothing' and is ONLY needed when Python requires a statement but you have nothing to put there yet. Once you add real code, pass becomes redundant. Think of pass like a bookmark for 'TODO' sections. Empty blocks are often code smells - if a block does nothing, why does it exist? Either implement it or remove it. Use ... (ellipsis) as an alternative to pass in stubs - it's becoming more common!",
        'severity': 'convention'
    },
    
    'singleton-comparison': {
        'title': "🎯 Use 'is' for Singleton Comparison",
        'explain': "When comparing to None, True, or False, use 'is' not '=='.",
        'how_to_fix': "Replace == with 'is' for None/True/False comparisons.",
        'wrong': "if value == None:\n    pass",
        'right': "if value is None:\n    pass",
        'learn': "💡 'is' checks identity (same object), '==' checks equality (same value). For singletons, use 'is'!",
        'severity': 'convention'
    },
    
    'missing-module-docstring': {
        'title': "📚 Missing Module Docstring",
        'explain': "Your Python file (module) doesn't have a docstring at the very top. Module docstrings are important because they're the first thing people see when they open your file or use help() on it. They should briefly explain what the module does and what's in it. It's like a book without a title page - people don't know what they're looking at! Even simple scripts benefit from a one-line module docstring.",
        'how_to_fix': "Add a module docstring at the very top of your file:\n1. Put it as the first line, before any imports\n2. Use triple quotes (\"\"\" or ''')\n3. For simple modules: one line explaining the purpose\n4. For complex modules: describe what it contains and how to use it\n5. You can use it for copyright/author info too",
        'wrong': "# my_module.py\nimport os\nimport sys\n\ndef helper():\n    pass",
        'right': '"""Utility functions for file operations.\n\nThis module provides helper functions for reading,\nwriting, and processing files safely.\n"""\nimport os\nimport sys\n\ndef helper():\n    """Helper function for file operations."""\n    pass',
        'learn': "💡 Module docstrings are like signs on doors - they tell people what's inside before they enter! They appear in help() output, documentation generators, and IDE tooltips. Professional Python packages always have module docstrings. Think of it as introducing yourself when you enter a room. One clear sentence can save someone minutes of confusion!",
        'severity': 'convention'
    },
    
    'empty-docstring': {
        'title': "📚 Empty Docstring",
        'explain': "You have an empty docstring - either fill it in or remove it.",
        'how_to_fix': "Add meaningful documentation or remove the empty docstring.",
        'wrong': 'def calculate():\n    """"""\n    return 42',
        'right': 'def calculate():\n    """Calculate and return 42."""\n    return 42',
        'learn': "💡 Empty docstrings are worse than no docstrings - they're misleading!",
        'severity': 'convention'
    },
    
    'superfluous-parens': {
        'title': "🎯 Unnecessary Parentheses",
        'explain': "These parentheses aren't needed.",
        'how_to_fix': "Remove the extra parentheses.",
        'wrong': "if (x > 5):\n    pass",
        'right': "if x > 5:\n    pass",
        'learn': "💡 Python doesn't require parentheses around conditions!",
        'severity': 'convention'
    },
    
    'missing-final-newline': {
        'title': "📝 Missing Final Newline",
        'explain': "Files should end with a newline character.",
        'how_to_fix': "Add a newline at the end of the file.",
        'wrong': "# File ends here without newline",
        'right': "# File ends here with newline\n",
        'learn': "💡 Final newlines are a Unix convention and help with git diffs!",
        'severity': 'convention'
    },
    
    'consider-using-f-string': {
        'title': "✨ Consider Using f-strings",
        'explain': "f-strings (Python 3.6+) are more readable and faster than .format() or %.",
        'how_to_fix': "Use f-strings for string formatting.",
        'wrong': "'Hello, {}'.format(name)",
        'right': "f'Hello, {name}'  # Cleaner!",
        'learn': "💡 f-strings are the modern Python way!",
        'severity': 'convention'
    },
    
    'bad-classmethod-argument': {
        'title': "📏 Class Method First Argument",
        'explain': "Class methods should have 'cls' as the first parameter, not 'self'.",
        'how_to_fix': "Change the first parameter to 'cls'.",
        'wrong': "@classmethod\ndef create(self):  # Should be cls!",
        'right': "@classmethod\ndef create(cls):  # Correct!",
        'learn': "💡 'cls' represents the class, 'self' represents an instance!",
        'severity': 'convention'
    },
    
    'wrong-import-position': {
        'title': "📦 Import Not at Top of File",
        'explain': "Imports should be at the top of the file, not scattered throughout.",
        'how_to_fix': "Move imports to the top of the file.",
        'wrong': "def calculate():\n    import math  # Import inside function!",
        'right': "import math  # At top\n\ndef calculate():",
        'learn': "💡 Imports at the top make dependencies clear!",
        'severity': 'convention'
    },
    
    'multiple-imports': {
        'title': "📦 Multiple Imports on One Line",
        'explain': "Import statements should be on separate lines for clarity.",
        'how_to_fix': "Put each import on its own line.",
        'wrong': "import os, sys, math",
        'right': "import os\nimport sys\nimport math",
        'learn': "💡 Separate imports are easier to read and manage!",
        'severity': 'convention'
    },

     'fixme': {
        'title': "📝 TODO/FIXME Comment",
        'explain': "You have a TODO, FIXME, or XXX comment marking unfinished work.",
        'how_to_fix': "Complete the task or track it in your issue system.",
        'wrong': "# TODO: Implement this later",
        'right': "# Track tasks in your issue system and clean up the code!",
        'learn': "💡 TODOs are reminders - don't forget to come back to them!",
        'severity': 'convention'
    },

    'missing-class-docstring': {
        'title': "📚 Missing Class Docstring",
        'explain': "Your class doesn't have a docstring explaining what it does.",
        'how_to_fix': "Add a docstring right after the class definition.",
        'wrong': "class DataProcessor:\n    def __init__(self):  # No docstring",
        'right': "class DataProcessor:\n    \"\"\"Processes data from various sources.\"\"\"\n    def __init__(self):",
        'learn': "💡 Class docstrings help others understand the purpose of your class!",
        'severity': 'convention'
    },

    'consider-using-dict-items': {
        'title': "💡 Use dict.items() for Iteration",
        'explain': "You're iterating over dictionary keys and then accessing values. Use .items() to get both at once!",
        'how_to_fix': "Replace 'for key in dict:' with 'for key, value in dict.items():'",
        'wrong': "for key in my_dict:\n    value = my_dict[key]  # Extra lookup!",
        'right': "for key, value in my_dict.items():  # Both at once!",
        'learn': "💡 .items() is more efficient and more Pythonic!",
        'severity': 'convention'
    },

    'use-maxsplit-arg': {
        'title': "💡 Use maxsplit Parameter",
        'explain': "When you only need to split into a fixed number of parts, use the maxsplit parameter for efficiency.",
        'how_to_fix': "Add maxsplit parameter: str.split(sep, maxsplit)",
        'wrong': "parts = text.split(':')  # Splits everything\nfirst = parts[0]\nrest = parts[1]  # Only need 2 parts",
        'right': "first, rest = text.split(':', 1)  # Split into 2 parts max",
        'learn': "💡 maxsplit makes split() more efficient when you know how many parts you need!",
        'severity': 'convention'
    },

    'invalid-sequence-index': {
        'title': "🔵 Invalid Sequence Index",
        'explain': "You're trying to access a sequence (like a list, string, or tuple) using an index, but the index type or usage is invalid. This usually happens when: 1) Using a variable that might not exist as an index, 2) Using a non-integer type as an index, or 3) Trying to index something that isn't a sequence. Python sequences can only be indexed with integers, and the variable used as an index must be defined and accessible.",
        'how_to_fix': "1. Make sure the variable used as an index is defined before use\n2. Ensure the index is an integer type\n3. Check that you're indexing an actual sequence (list, tuple, string)\n4. Verify the variable scope - is it defined in the current context?",
        'wrong': "# Using undefined variable as index\nif number % 2 == 0:  # 'number' not defined!\n    print('even')\n\n# Using wrong type as index\nmy_list = [1, 2, 3]\nindex = '0'  # String, not integer\nprint(my_list[index])  # Error!",
        'right': "# Define variable before using as index\nnumber = 10  # ✅ Defined first\nif number % 2 == 0:\n    print('even')\n\n# Use integer for indexing\nmy_list = [1, 2, 3]\nindex = 0  # ✅ Integer\nprint(my_list[index])  # Works!",
        'learn': "💡 Convention tip: Always define variables before using them in any context, including as sequence indices. Python requires explicit variable definition - there's no 'implicit' or 'auto-declared' variables. Also remember: sequences use integer indices (0, 1, 2...), not strings or floats!",
        'severity': 'convention'
    },



    # ============================================
    # REFACTORING (Optimization Opportunities)
    # ============================================
    
    'too-many-arguments': {
        'title': "🔧 Too Many Function Parameters",
        'explain': "Your function takes too many parameters (typically more than 5-7). This makes the function hard to call because users have to remember the order and meaning of many arguments, leading to mistakes. It also suggests the function might be doing too much or that related parameters should be grouped together. It's like a restaurant server trying to carry 10 plates at once - unwieldy and error-prone! This is a code smell indicating poor function design.",
        'how_to_fix': "Reduce parameter count:\n1. Group related parameters into a class or dataclass: UserInfo(name, email, phone)\n2. Use a dictionary for configuration: create_user(name, **options)\n3. Split into smaller functions that each take fewer parameters\n4. Use default values for optional parameters\n5. Consider if some parameters could be instance variables (make it a class method)",
        'wrong': "def create_user(name, age, email, phone, address, \n                city, state, zip_code, country, \n                occupation, salary):\n    # 11 parameters - hard to remember!\n    pass\n\n# Calling is error-prone:\ncreate_user('Alice', 30, 'alice@email.com', \n           '555-1234', '123 Main St', \n           'NYC', 'NY', '10001', 'USA',\n           'Engineer', 80000)  # Did I get the order right?",
        'right': "# Group related data:\n@dataclass\nclass UserInfo:\n    name: str\n    age: int\n    contact: ContactInfo\n    address: Address\n    employment: Employment\n\ndef create_user(user_info: UserInfo):\n    # Just one well-structured parameter!\n    pass\n\n# OR use dictionary for options:\ndef create_user(name, age, **options):\n    email = options.get('email')\n    phone = options.get('phone')\n    # Flexible and clear!\n\n# Calling is much clearer:\nuser = UserInfo(\n    name='Alice',\n    age=30,\n    contact=contact_info,\n    address=address_info,\n    employment=job_info\n)\ncreate_user(user)",
        'learn': "💡 The ideal function has 0-3 parameters. Beyond 5 parameters, it becomes hard to use and remember. This is one of the strongest signals that you need to refactor! Group related parameters into objects (classes or named tuples), use **kwargs for flexible options, or split into multiple focused functions. Think of parameters like ingredients - if you need too many, maybe you're making multiple dishes at once instead of one!",
        'severity': 'refactor'
    },
    
    'too-many-locals': {
        'title': "🔧 Too Many Local Variables",
        'explain': "Your function has too many local variables (typically more than 15), which is a strong sign it's doing too much! Each variable represents a piece of state the function is tracking, and humans can only keep track of so many things at once. When you see many variables, it usually means: 1) The function has multiple responsibilities, 2) Some variables could be grouped into objects, or 3) Parts of the logic should be extracted into helper functions. It's like juggling 20 balls at once - you're bound to drop something!",
        'how_to_fix': "Reduce local variables:\n1. Split function into smaller focused functions, each with fewer variables\n2. Group related variables into a class or named tuple\n3. Extract complex calculations into separate functions\n4. Use intermediate functions to break up logic\n5. Ask: 'Is this function doing one thing or multiple things?'",
        'wrong': "def process_order():\n    # Function with 20+ variables:\n    customer_name = get_name()\n    customer_email = get_email()\n    customer_phone = get_phone()\n    product_id = get_product()\n    product_name = get_product_name()\n    product_price = get_price()\n    quantity = get_quantity()\n    subtotal = calculate_subtotal()\n    tax_rate = get_tax_rate()\n    tax_amount = calculate_tax()\n    shipping_address = get_address()\n    shipping_method = get_method()\n    shipping_cost = calculate_shipping()\n    discount_code = get_discount()\n    discount_amount = calculate_discount()\n    total = calculate_total()\n    payment_method = get_payment()\n    # ... doing too much!",
        'right': "# Split into focused functions:\ndef process_order():\n    customer = get_customer_info()\n    order_items = get_order_items()\n    pricing = calculate_pricing(order_items)\n    shipping = process_shipping(customer)\n    payment = process_payment(pricing.total)\n    return create_order(customer, order_items, pricing, shipping, payment)\n\ndef get_customer_info():\n    # Fewer variables, focused purpose\n    return Customer(name, email, phone)\n\ndef calculate_pricing(items):\n    # Calculation logic isolated\n    return Pricing(subtotal, tax, discount, total)",
        'learn': "💡 Too many local variables is one of the clearest signals that a function is doing too much! The 'Single Responsibility Principle' says functions should do ONE thing. If you're tracking 15+ pieces of data, you're probably doing 3-4 things. Extract logical chunks into helper functions. Each function should fit in your working memory - if you can't hold all the variables in your head, it's too complex. Break it down!",
        'severity': 'refactor'
    },
    
    'too-many-branches': {
        'title': "🔧 Too Many Conditional Branches",
        'explain': "Your function has too many if/elif/else branches (typically more than 12), making it complex and hard to test. Each branch is a different path through the code, and with many branches you have exponential combinations to test! Long if-elif chains usually mean you're doing dispatch logic (routing to different handlers) which can be done more elegantly. It's like having a receptionist who asks 20 questions to figure out where to send you - inefficient and error-prone!",
        'how_to_fix': "Replace branches with better patterns:\n1. Dictionary dispatch: map values to functions\n2. Polymorphism: use classes with different behaviors\n3. Strategy pattern: pass in the behavior\n4. Guard clauses: handle edge cases early with returns\n5. Lookup tables: map inputs to outputs directly",
        'wrong': "def handle_request(request_type):\n    if request_type == 'GET':\n        return handle_get()\n    elif request_type == 'POST':\n        return handle_post()\n    elif request_type == 'PUT':\n        return handle_put()\n    elif request_type == 'DELETE':\n        return handle_delete()\n    elif request_type == 'PATCH':\n        return handle_patch()\n    # ... 10 more elif statements\n    # Hard to read, test, and maintain!",
        'right': "# Dictionary dispatch pattern:\ndef handle_request(request_type):\n    handlers = {\n        'GET': handle_get,\n        'POST': handle_post,\n        'PUT': handle_put,\n        'DELETE': handle_delete,\n        'PATCH': handle_patch,\n        # Add more easily!\n    }\n    handler = handlers.get(request_type, handle_unknown)\n    return handler()\n\n# OR use polymorphism:\nclass GetHandler:\n    def handle(self): ...\n\nclass PostHandler:\n    def handle(self): ...\n\nhandlers = {\n    'GET': GetHandler(),\n    'POST': PostHandler(),\n}\nhandlers[request_type].handle()",
        'learn': "💡 Long if-elif chains are dispatch logic in disguise! Instead of asking 'which case am I?', use a dictionary to look up what to do. This is: 1) More scalable (easy to add cases), 2) More testable (each handler tests separately), 3) More readable (clear mapping), 4) More maintainable (no giant function). This is a fundamental refactoring pattern - learn it! When you see many branches doing similar structures, think: dictionary, polymorphism, or strategy pattern.",
        'severity': 'refactor'
    },
    
    'too-many-return-statements': {
        'title': "🔧 Too Many Return Statements",
        'explain': "Multiple return statements make functions harder to understand and debug.",
        'how_to_fix': "Consolidate logic to have fewer return points.",
        'wrong': "def check_value(x):\n    if x < 0: return 'negative'\n    if x == 0: return 'zero'\n    if x < 10: return 'small'\n    # ... many more returns",
        'right': "def check_value(x):\n    if x < 0:\n        result = 'negative'\n    elif x == 0:\n        result = 'zero'\n    # ...\n    return result",
        'learn': "💡 Single return point makes functions easier to debug and understand!",
        'severity': 'refactor'
    },
    
    'no-else-return': {
        'title': "💡 Unnecessary else After Return",
        'explain': "When you return in an if block, the else is unnecessary.",
        'how_to_fix': "Remove the else clause and unindent the code.",
        'wrong': "def get_grade(score):\n    if score >= 90:\n        return 'A'\n    else:\n        return 'B'",
        'right': "def get_grade(score):\n    if score >= 90:\n        return 'A'\n    return 'B'  # No else needed!",
        'learn': "💡 After a return, else is unreachable anyway. Keep it simple!",
        'severity': 'refactor'
    },
    
    'simplifiable-if-statement': {
        'title': "💡 Simplify If-Else to Direct Return",
        'explain': "Your function uses if-else to return True or False based on a condition, but the condition itself IS already True or False! This is a very common beginner pattern that adds unnecessary code. You're essentially saying 'if this is true, return true, otherwise return false' - but you can just return the 'this is true' part directly! It's like asking 'Is it raining?' and responding 'If it's raining, then yes, it's raining, otherwise no, it's not raining' instead of just looking outside.",
        'how_to_fix': "Return the condition directly:\n1. Delete the if-else structure\n2. Return the boolean expression itself: return age >= 18\n3. Works for any boolean expression: comparisons, 'in', 'and', 'or', etc.\n4. This is cleaner, shorter, and more Pythonic",
        'wrong': "def is_adult(age):\n    if age >= 18:\n        return True\n    else:\n        return False  # Verbose!\n\ndef is_valid(x):\n    if x > 0 and x < 100:\n        return True\n    else:\n        return False  # Unnecessary if-else!\n\ndef contains_item(items, target):\n    if target in items:\n        return True\n    return False  # Same pattern!",
        'right': "def is_adult(age):\n    return age >= 18  # Clean and direct!\n\ndef is_valid(x):\n    return 0 < x < 100  # Even cleaner with chained comparison!\n\ndef contains_item(items, target):\n    return target in items  # Direct boolean return\n\n# The condition IS the answer:\ndef is_even(n):\n    return n % 2 == 0  # Already returns bool!\n\ndef should_process(data):\n    return len(data) > 0 and data[0].is_valid()",
        'learn': "💡 Comparison operators return booleans directly! There's no need to wrap them in if-else. This is one of the most common unnecessary patterns in beginner code. The condition you're checking (age >= 18) is ALREADY a boolean (True/False), so just return it! This same principle applies to: comparisons (>, <, ==), membership tests (in), isinstance(), and any other boolean expression. Professional Python code returns conditions directly. Shorter is better when it's also clearer!",
        'severity': 'refactor'
    },
    
    'consider-using-dict-comprehension': {
        'title': "⚡ Use Dictionary Comprehension",
        'explain': "You can create dictionaries more elegantly with comprehensions.",
        'how_to_fix': "Use {key: value for ...} syntax.",
        'wrong': "result = {}\nfor item in items:\n    result[item.id] = item.name",
        'right': "result = {item.id: item.name for item in items}",
        'learn': "💡 Comprehensions are faster and more Pythonic!",
        'severity': 'refactor'
    },
    
    'consider-using-set-comprehension': {
        'title': "⚡ Use Set Comprehension",
        'explain': "You can create sets more elegantly with comprehensions.",
        'how_to_fix': "Use {value for ...} syntax.",
        'wrong': "result = set()\nfor item in items:\n    result.add(item.lower())",
        'right': "result = {item.lower() for item in items}",
        'learn': "💡 Set comprehensions are cleaner and faster!",
        'severity': 'refactor'
    },
    
    'unnecessary-comprehension': {
        'title': "💡 Unnecessary List Comprehension",
        'explain': "This list comprehension can be simplified.",
        'how_to_fix': "Use the iterable directly or built-in functions.",
        'wrong': "items = [x for x in range(10)]",
        'right': "items = list(range(10))  # Direct conversion",
        'learn': "💡 Don't use comprehensions when direct conversion is clearer!",
        'severity': 'refactor'
    },
    
    'consider-using-in': {
        'title': "💡 Use 'in' Operator",
        'explain': "Multiple 'or' comparisons can be simplified with 'in'.",
        'how_to_fix': "Use 'value in (a, b, c)' instead of multiple 'or'.",
        'wrong': "if x == 1 or x == 2 or x == 3:\n    pass",
        'right': "if x in (1, 2, 3):\n    pass",
        'learn': "💡 'in' is more readable and extensible!",
        'severity': 'refactor'
    },
    
    'chained-comparison': {
        'title': "💡 Use Chained Comparison",
        'explain': "You can chain comparison operators in Python.",
        'how_to_fix': "Chain the comparisons directly.",
        'wrong': "if x > 0 and x < 10:\n    pass",
        'right': "if 0 < x < 10:\n    pass",
        'learn': "💡 Chained comparisons are more readable and Pythonic!",
        'severity': 'refactor'
    },
    
    'consider-using-generator': {
        'title': "⚡ Consider Using Generator",
        'explain': "For large data, generators use less memory than lists.",
        'how_to_fix': "Use parentheses instead of square brackets for generator expression.",
        'wrong': "total = sum([x**2 for x in range(1000000)])  # Creates huge list!",
        'right': "total = sum(x**2 for x in range(1000000))  # Uses generator",
        'learn': "💡 Generators process one item at a time, saving memory!",
        'severity': 'refactor'
    },
    
    'inconsistent-return-statements': {
        'title': "🔧 Inconsistent Return Statements",
        'explain': "Some paths return a value, others return None implicitly.",
        'how_to_fix': "Make sure all paths explicitly return a value.",
        'wrong': "def get_value(x):\n    if x > 0:\n        return x  # Returns value\n    # Implicitly returns None!",
        'right': "def get_value(x):\n    if x > 0:\n        return x\n    return None  # Explicit!",
        'learn': "💡 Be explicit about what your function returns!",
        'severity': 'refactor'
    },
    
    'useless-return': {
        'title': "💡 Useless Return Statement",
        'explain': "This return statement at the end of a function is unnecessary.",
        'how_to_fix': "Remove the return statement.",
        'wrong': "def process():\n    do_something()\n    return  # Unnecessary!",
        'right': "def process():\n    do_something()  # Will return None automatically",
        'learn': "💡 Functions return None by default when they end!",
        'severity': 'refactor'
    },
    
    'consider-using-get': {
        'title': "💡 Use dict.get() for Safety",
        'explain': "Dictionary get() is safer than direct access - it won't raise KeyError.",
        'how_to_fix': "Use .get() with a default value.",
        'wrong': "value = data[key]  # KeyError if missing!",
        'right': "value = data.get(key, default_value)  # Safe!",
        'learn': "💡 get() returns None (or your default) if key is missing!",
        'severity': 'refactor'
    },
    
    'consider-using-with': {
        'title': "⚡ Use Context Manager (with statement)",
        'explain': "You're manually managing a resource (file, connection, lock) that should be handled by a 'with' statement (context manager). Manual management is error-prone because if an exception occurs, your cleanup code (close, unlock, disconnect) might never run, causing resource leaks. 'with' statements guarantee cleanup happens no matter what - even if errors occur. It's like having an automatic door closer vs. remembering to close the door yourself every time!",
        'how_to_fix': "Use 'with' for automatic resource management:\n1. Files: with open('file.txt') as f: ...\n2. Locks: with my_lock: ...\n3. Database connections: with connection: ...\n4. Network connections: with socket.connect() as conn: ...\n5. Cleanup happens automatically when the with block ends",
        'wrong': "# File without with:\nf = open('data.txt')\ndata = f.read()\nf.close()  # Might not run if error!\n\n# Lock without with:\nlock.acquire()\ntry:\n    critical_section()\nfinally:\n    lock.release()  # Verbose!\n\n# Multiple resources:\nf1 = open('input.txt')\nf2 = open('output.txt')\nprocess(f1, f2)\nf1.close()\nf2.close()  # Easy to forget!",
        'right': "# File with 'with':\nwith open('data.txt') as f:\n    data = f.read()  # Auto-closes!\n\n# Lock with 'with':\nwith lock:\n    critical_section()  # Auto-releases!\n\n# Multiple resources:\nwith open('input.txt') as f1, open('output.txt') as f2:\n    process(f1, f2)  # Both auto-close!\n\n# Nested contexts:\nwith database.connect() as conn:\n    with conn.cursor() as cursor:\n        cursor.execute(query)",
        'learn': "💡 Context managers (with statements) implement the 'Resource Acquisition Is Initialization' pattern - resources are automatically cleaned up when you're done, even if errors occur! This prevents resource leaks (open files, locked locks, hanging connections). Every resource that needs cleanup should use 'with'. You can even create your own context managers with __enter__ and __exit__ methods! Think of 'with' as a guaranteed cleanup crew that works no matter what happens.",
        'severity': 'refactor'
    },
    
    'too-many-instance-attributes': {
        'title': "🔧 Too Many Instance Attributes",
        'explain': "This class has too many attributes, making it complex.",
        'how_to_fix': "Consider breaking into smaller classes.",
        'wrong': "class User:\n    # 15+ attributes...",
        'right': "class User:\n    # Basic attributes\nclass UserProfile:\n    # Profile-specific attributes",
        'learn': "💡 Classes should have a single, well-defined responsibility!",
        'severity': 'refactor'
    },
    
    'too-many-statements': {
        'title': "🔧 Function Has Too Many Statements",
        'explain': "Your function has too many statements (typically 50+), making it a 'wall of code' that's hard to understand, test, and maintain. Long functions usually have multiple logical sections that should be extracted into their own functions. When a function is long, readers can't see the 'big picture' - they get lost in details. Testing is also hard because you can't test individual pieces. It's like trying to read a book chapter that's 200 pages long with no section breaks!",
        'how_to_fix': "Break into smaller functions:\n1. Identify logical sections (usually separated by blank lines or comments)\n2. Extract each section into a well-named helper function\n3. The main function becomes a high-level outline of steps\n4. Each helper function should be 5-30 lines\n5. Name functions after what they DO, not what they contain",
        'wrong': "def process_data():\n    # 100+ lines doing everything:\n    # Read file\n    file = open('data.txt')\n    lines = file.readlines()\n    file.close()\n    \n    # Parse data\n    data = []\n    for line in lines:\n        parts = line.split(',')\n        data.append(parts)\n    \n    # Validate data  \n    valid = []\n    for row in data:\n        if len(row) == 3:\n            valid.append(row)\n    \n    # Transform data\n    transformed = []\n    for row in valid:\n        # ... 20 more lines\n    \n    # Calculate statistics\n    # ... 30 more lines\n    \n    # Generate report\n    # ... 30 more lines\n    \n    return result",
        'right': "# Split into focused functions:\ndef process_data():\n    '''Main orchestrator - shows the big picture'''\n    raw_data = read_data_file('data.txt')\n    parsed = parse_csv_data(raw_data)\n    validated = validate_data(parsed)\n    transformed = transform_data(validated)\n    stats = calculate_statistics(transformed)\n    report = generate_report(stats)\n    return report\n\ndef read_data_file(filename):\n    '''Focused: just reading'''\n    with open(filename) as f:\n        return f.readlines()\n\ndef parse_csv_data(lines):\n    '''Focused: just parsing'''\n    return [line.split(',') for line in lines]\n\ndef validate_data(data):\n    '''Focused: just validation'''\n    return [row for row in data if len(row) == 3]",
        'learn': "💡 Long functions are the enemy of maintainability! Functions should be short enough to fit on one screen (typically 5-50 lines). The magic: extract chunks into well-named functions. The main function becomes readable documentation showing the high-level flow. Each helper function is small, testable, and focused on one thing. This is called 'Extract Function' refactoring - one of the most important skills! Think of functions like paragraphs: each should express one complete thought.",
        'severity': 'refactor'
    },
    
    'cyclic-import': {
        'title': "🔧 Cyclic Import Detected",
        'explain': "Two modules are importing each other, creating a circular dependency.",
        'how_to_fix': "Restructure to break the cycle - move shared code to a third module.",
        'wrong': "# a.py imports b.py\n# b.py imports a.py",
        'right': "# Move shared code to c.py\n# Both a.py and b.py import c.py",
        'learn': "💡 Circular imports cause initialization problems!",
        'severity': 'refactor'
    },
    
    'duplicate-code': {
        'title': "🔧 Duplicate Code Detected",
        'explain': "Similar or identical code appears in multiple places.",
        'how_to_fix': "Extract duplicated code into a shared function.",
        'wrong': "# Same code in multiple functions",
        'right': "def shared_logic():\n    # Common code\n# Call from multiple places",
        'learn': "💡 Don't Repeat Yourself (DRY) - extract common code!",
        'severity': 'refactor'
    },
    
    'no-else-raise': {
        'title': "💡 Unnecessary else After raise",
        'explain': "After raising an exception, else is unreachable.",
        'how_to_fix': "Remove the else clause.",
        'wrong': "if error:\n    raise ValueError()\nelse:\n    process()",
        'right': "if error:\n    raise ValueError()\nprocess()  # No else needed",
        'learn': "💡 Code after raise won't execute, so else is redundant!",
        'severity': 'refactor'
    },
    
    'no-else-break': {
        'title': "💡 Unnecessary else After break",
        'explain': "After break, else is unnecessary.",
        'how_to_fix': "Remove the else clause.",
        'wrong': "for item in items:\n    if condition:\n        break\n    else:\n        process()",
        'right': "for item in items:\n    if condition:\n        break\n    process()",
        'learn': "💡 break exits the loop, making else redundant!",
        'severity': 'refactor'
    },
    
    'no-else-continue': {
        'title': "💡 Unnecessary else After continue",
        'explain': "After continue, else is unnecessary.",
        'how_to_fix': "Remove the else clause.",
        'wrong': "for item in items:\n    if skip:\n        continue\n    else:\n        process()",
        'right': "for item in items:\n    if skip:\n        continue\n    process()",
        'learn': "💡 continue skips to next iteration, making else redundant!",
        'severity': 'refactor'
    },
    
    'consider-using-sys-exit': {
        'title': "💡 Use sys.exit() Instead",
        'explain': "Use sys.exit() instead of exit() for better clarity.",
        'how_to_fix': "Import sys and use sys.exit().",
        'wrong': "exit(0)  # Built-in exit",
        'right': "import sys\nsys.exit(0)  # Explicit!",
        'learn': "💡 sys.exit() is more explicit and works in all contexts!",
        'severity': 'refactor'
    },
    
    'use-a-generator': {
        'title': "⚡ Use Generator Instead",
        'explain': "Creating a full list in memory is wasteful - use a generator!",
        'how_to_fix': "Return a generator instead of building a list.",
        'wrong': "def get_numbers():\n    result = []\n    for i in range(1000000):\n        result.append(i * 2)\n    return result",
        'right': "def get_numbers():\n    for i in range(1000000):\n        yield i * 2  # Generator!",
        'learn': "💡 Generators are memory-efficient for large datasets!",
        'severity': 'refactor'
    },
    
    'consider-using-min-builtin': {
        'title': "💡 Use min() Builtin",
        'explain': "Python's min() builtin is clearer than manual comparison.",
        'how_to_fix': "Use min() directly.",
        'wrong': "smallest = a if a < b else b",
        'right': "smallest = min(a, b)  # Clearer!",
        'learn': "💡 Built-in functions are optimized and more readable!",
        'severity': 'refactor'
    },
    
    'consider-using-max-builtin': {
        'title': "💡 Use max() Builtin",
        'explain': "Python's max() builtin is clearer than manual comparison.",
        'how_to_fix': "Use max() directly.",
        'wrong': "largest = a if a > b else b",
        'right': "largest = max(a, b)  # Clearer!",
        'learn': "💡 Built-in functions are optimized and more readable!",
        'severity': 'refactor'
    },
    
    'super-with-arguments': {
        'title': "💡 Use super() Without Arguments",
        'explain': "In Python 3, super() doesn't need arguments.",
        'how_to_fix': "Remove the class and self arguments.",
        'wrong': "super(MyClass, self).__init__()",
        'right': "super().__init__()  # Python 3 way!",
        'learn': "💡 Python 3's super() is simpler and less error-prone!",
        'severity': 'refactor'
    },
    
    'use-list-literal': {
        'title': "💡 Use List Literal []",
        'explain': "Use [] instead of list() for clarity.",
        'how_to_fix': "Replace list() with [].",
        'wrong': "items = list()",
        'right': "items = []  # Cleaner!",
        'learn': "💡 Literals are more readable than constructors!",
        'severity': 'refactor'
    },
    
    'use-dict-literal': {
        'title': "💡 Use Dict Literal {}",
        'explain': "Use {} instead of dict() for clarity.",
        'how_to_fix': "Replace dict() with {}.",
        'wrong': "data = dict()",
        'right': "data = {}  # Cleaner!",
        'learn': "💡 Literals are more readable than constructors!",
        'severity': 'refactor'
    },
    
    'too-many-nested-blocks': {
        'title': "🔧 Too Many Nested Blocks (Deep Nesting)",
        'explain': "Your code has too many levels of nesting (typically 4+ levels deep), making it extremely hard to read and understand. Each level of nesting adds cognitive load - readers have to keep track of 'where am I in the nested structure?' Deep nesting is called the 'Arrow Anti-Pattern' because the code looks like an arrow pointing right. It usually indicates complex conditional logic that should be simplified. It's like nesting Russian dolls - the deeper you go, the harder it is to remember where you are!",
        'how_to_fix': "Flatten the nesting:\n1. Guard clauses: handle errors/edge cases early with return\n2. Invert conditions: if not valid: return → less nesting\n3. Extract inner blocks into functions\n4. Combine conditions: if a and b: instead of if a: if b:\n5. Use early continues in loops to skip processing",
        'wrong': "def process_items(items):\n    for item in items:\n        if item.is_valid():\n            if item.is_active():\n                if item.needs_processing():\n                    if not item.is_locked():\n                        if item.has_data():\n                            # Finally do work - 5 levels deep!\n                            result = item.process()\n                            if result.success:\n                                save(result)\n                            else:\n                                log_error(result)\n                        else:\n                            skip(item)\n                    else:\n                        wait(item)",
        'right': "# Flattened with guard clauses:\ndef process_items(items):\n    for item in items:\n        # Handle invalid cases early\n        if not item.is_valid():\n            continue\n        if not item.is_active():\n            continue\n        if not item.needs_processing():\n            continue\n        if item.is_locked():\n            wait(item)\n            continue\n        if not item.has_data():\n            skip(item)\n            continue\n            \n        # Main logic - only 1 level deep!\n        result = item.process()\n        if result.success:\n            save(result)\n        else:\n            log_error(result)\n\n# OR extract to function:\ndef process_item(item):\n    if not should_process(item):\n        return\n    result = item.process()\n    handle_result(result)",
        'learn': "💡 'Flat is better than nested' - Python's Zen! Each nesting level makes code exponentially harder to read. The solution: guard clauses (early returns/continues) and extraction. Guard clauses flip the logic: instead of 'if valid: do_stuff', use 'if not valid: return'. This keeps the 'happy path' at the lowest indentation level. Aim for maximum 3 levels of nesting. If you're deeper, you're doing too much in one place - extract functions! Code should flow down, not dive deep.",
        'severity': 'refactor'
    },
    
    'consider-using-join': {
        'title': "⚡ Use str.join() for Concatenation",
        'explain': "join() is much faster than repeated string concatenation.",
        'how_to_fix': "Use ''.join() or ' '.join().",
        'wrong': "result = ''\nfor word in words:\n    result += word",
        'right': "result = ''.join(words)  # Much faster!",
        'learn': "💡 join() is O(n), += in loop is O(n²)!",
        'severity': 'refactor'
    },
    
    'no-self-use': {
        'title': "🔧 Method Doesn't Use 'self'",
        'explain': "This method doesn't access instance data - should it be a static method?",
        'how_to_fix': "Either use instance data or make it a static method with @staticmethod.",
        'wrong': "class MyClass:\n    def calculate(self, x, y):\n        return x + y  # Doesn't use self!",
        'right': "class MyClass:\n    @staticmethod\n    def calculate(x, y):\n        return x + y",
        'learn': "💡 Static methods signal that a method doesn't depend on instance state!",
        'severity': 'refactor'
    },
    
    'too-few-public-methods': {
        'title': "🔧 Class Has Too Few Methods",
        'explain': "This class has very few methods - is it really needed, or should it be a function/dict?",
        'how_to_fix': "Consider if this could be a simple function or data structure instead.",
        'wrong': "class Config:\n    def __init__(self):\n        self.value = 42  # Just data!",
        'right': "# Just use a dict or namedtuple\nconfig = {'value': 42}",
        'learn': "💡 Not everything needs to be a class!",
        'severity': 'refactor'
    },
    
    'consider-merging-isinstance': {
        'title': "💡 Merge isinstance() Calls",
        'explain': "Multiple isinstance() checks can be combined.",
        'how_to_fix': "Pass a tuple of types to isinstance().",
        'wrong': "if isinstance(x, int) or isinstance(x, float):",
        'right': "if isinstance(x, (int, float)):  # Combined!",
        'learn': "💡 isinstance() accepts a tuple of types!",
        'severity': 'refactor'
    },
    
    'simplifiable-condition': {
        'title': "💡 Simplifiable Condition",
        'explain': "This condition can be simplified.",
        'how_to_fix': "Simplify the boolean logic.",
        'wrong': "if (x > 5) == True:",
        'right': "if x > 5:  # Simple!",
        'learn': "💡 Keep conditions simple and direct!",
        'severity': 'refactor'
    },
    
    'simplify-boolean-expression': {
        'title': "💡 Simplify Boolean Logic",
        'explain': "Your boolean expression can be simplified using boolean algebra rules. Common issues: double negatives (not (not x)), redundant comparisons (x == True), or complex expressions that can be rewritten more clearly. Complicated boolean logic is hard to read and understand - simpler is better! It's like saying 'it's not true that it's not raining' instead of just 'it's raining'. Your code works, but it's unnecessarily confusing.",
        'how_to_fix': "Apply simplification rules:\n1. Double negative: not (not x) → x\n2. Redundant comparison: x == True → x\n3. DeMorgan's laws: not (a and b) → (not a) or (not b)\n4. Not equals: not (x == y) → x != y\n5. Remove redundant parentheses: (x) and (y) → x and y",
        'wrong': "# Double negative:\nif not (not is_ready):\n    start()\n\n# Redundant comparison:\nif (x > 5) == True:\n    process()\n\n# Overcomplicated:\nif not (age < 18):\n    allow()  # Just use age >= 18!\n\n# Complex DeMorgan:\nif not (is_valid and is_ready):\n    wait()  # Confusing!",
        'right': "# Simplified double negative:\nif is_ready:\n    start()\n\n# Remove redundant comparison:\nif x > 5:\n    process()\n\n# Clearer comparison:\nif age >= 18:\n    allow()\n\n# DeMorgan's law applied:\nif not is_valid or not is_ready:\n    wait()  # Much clearer!\n\n# More examples:\nif x != y:  # Not: if not (x == y)\nif a and b:  # Not: if (a) and (b)\nif not (x in items):  # Better: if x not in items",
        'learn': "💡 Boolean algebra has rules for simplification, just like regular algebra! Double negatives cancel out, redundant checks can be removed, and complex expressions can often be rewritten more clearly. The goal is code that's easy to read and understand at a glance. Remember: not (a and b) = (not a) or (not b), and Python has 'x not in items' which is clearer than 'not (x in items)'. Simpler boolean logic = fewer bugs!",
        'severity': 'refactor'
    },
    
    'consider-using-ternary': {
        'title': "💡 Use Ternary Operator",
        'explain': "This if-else can be replaced with a ternary expression.",
        'how_to_fix': "Use: value_if_true if condition else value_if_false",
        'wrong': "if x > 0:\n    result = 'positive'\nelse:\n    result = 'negative'",
        'right': "result = 'positive' if x > 0 else 'negative'",
        'learn': "💡 Ternary expressions are concise for simple conditions!",
        'severity': 'refactor'
    },
    
    'unnecessary-dict-index-lookup': {
        'title': "💡 Avoid Redundant Dict Lookup",
        'explain': "You're looking up the same key multiple times - store it once!",
        'how_to_fix': "Store the value in a variable.",
        'wrong': "if 'key' in d:\n    x = d['key']\n    y = d['key'] * 2  # Lookup twice!",
        'right': "value = d.get('key')\nif value:\n    x = value\n    y = value * 2",
        'learn': "💡 Each dictionary lookup has a cost - cache the result!",
        'severity': 'refactor'
    },

    'comparison-with-itself': {
        'title': "⚠️ Comparing Variable with Itself",
        'explain': "You're comparing a variable to itself, which is always True (or False for !=). This is likely a bug!",
        'how_to_fix': "Check if you meant to compare with a different variable.",
        'wrong': "if value == value:  # Always True!\n    process()",
        'right': "if value == other_value:  # Compare different things",
        'learn': "💡 Comparing a variable to itself is pointless - it's always True! Probably a typo!",
        'severity': 'refactor'
    },

    'too-complex': {
        'title': "🔧 Code Complexity Too High",
        'explain': "Your function has too many decision points (if/elif/for/while), making it hard to understand and test.",
        'how_to_fix': "Break the function into smaller, simpler functions.",
        'wrong': "def process(data):\n    # 50+ lines with many if/elif/for statements",
        'right': "def process(data):\n    validated = validate(data)\n    transformed = transform(validated)\n    return save(transformed)",
        'learn': "💡 Keep functions simple! If it's complex, break it into smaller pieces!",
        'severity': 'refactor'
    },

    'unnecessary-list-index-lookup': {
        'title': "💡 Avoid Unnecessary List Indexing",
        'explain': "You're using enumerate() but only using the index to look up values. Just iterate directly!",
        'how_to_fix': "If you don't need the index, iterate over the list directly.",
        'wrong': "for i, _ in enumerate(items):\n    print(items[i])  # Unnecessary indexing!",
        'right': "for item in items:\n    print(item)  # Direct access!",
        'learn': "💡 Only use enumerate() when you actually need both index AND value!",
        'severity': 'refactor'
    },

    
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
    
    def get_explanation(self, error_code, symbol=''):
        """
        Get structured educational explanation for an error code
        
        Args:
            error_code: Pylint error code (e.g., 'E0602')
            symbol: Optional symbol/variable name involved in the error
            
        Returns:
            Dictionary with formatted explanation or None
        """
        # Map error code to rule name
        rule_name = self.error_rules.get(error_code)
        if not rule_name:
            return None
        
        # Get explanation template
        explanation = self.explanations.get(rule_name)
        if not explanation:
            return None
        
        # Format explanation with symbol if provided (use fallback if symbol is None)
        safe_symbol = symbol if symbol else 'this identifier'
        
        formatted_explanation = {
            'title': explanation['title'],
            'explain': explanation['explain'].format(symbol=safe_symbol) if '{symbol}' in explanation['explain'] else explanation['explain'],
            'how_to_fix': explanation['how_to_fix'].format(symbol=safe_symbol) if '{symbol}' in explanation['how_to_fix'] else explanation['how_to_fix'],
            'wrong': explanation['wrong'],
            'right': explanation['right'],
            'learn': explanation['learn'],
            'severity': explanation['severity']
        }
        
        return formatted_explanation
    
    def translate_error(self, error_code, symbol=''):
        """
        Legacy method for backwards compatibility
        Returns formatted message string
        """
        explanation = self.get_explanation(error_code, symbol)
        if not explanation:
            return f"Error {error_code}: Check Python documentation"
        
        # Format as structured message
        message = f"{explanation['title']}\n\n"
        message += f"📋 EXPLAIN: {explanation['explain']}\n\n"
        message += f"🔧 HOW TO FIX: {explanation['how_to_fix']}\n\n"
        message += f"❌ WRONG:\n{explanation['wrong']}\n\n"
        message += f"✅ RIGHT:\n{explanation['right']}\n\n"
        message += f"📚 LEARN: {explanation['learn']}"
        
        return message

    def translate_message(self, error_code, line, symbol=''):
        """
        Translate error into structured JSON format for easy frontend parsing
        
        Args:
            error_code: Pylint error code (e.g., 'E0602')
            line: Line number where error occurs
            symbol: Optional symbol/variable name involved in the error
            
        Returns:
            Dictionary with structured feedback fields
        """
        explanation = self.get_explanation(error_code, symbol)
        
        if not explanation:
            # ✅ Detect type from Pylint error code prefix
            detected_type = 'error'  # default
            type_name = 'Unknown Error'
            
            if error_code.startswith('E') or error_code.startswith('F'):
                detected_type = 'error'
                type_name = 'Error'
            elif error_code.startswith('W'):
                detected_type = 'warning'
                type_name = 'Warning'
            elif error_code.startswith('C'):
                detected_type = 'convention'
                type_name = 'Convention'
            elif error_code.startswith('R'):
                detected_type = 'refactor'
                type_name = 'Refactor'
            
            # Fallback for unknown error codes
            return {
                'type': detected_type,
                'line': line,
                'message': f"Unknown error code: {error_code}",
                'code': error_code,
                'severity': detected_type,
                'structured': {
                    'title': f'❓ Unknown {type_name} ({error_code})',
                    'sections': [
                        {
                            'icon': '📋',
                            'heading': 'Description',
                            'content': f"Error code {error_code} is not in our database yet. Based on the code prefix, this is a {type_name.lower()}. Check Pylint documentation for more details about this specific code.",
                            'type': 'explain'
                        }
                    ]
                }
            }
        
        # DEBUG: Print what we're returning
        print(f"[RULE ENGINE] Returning structured data for {error_code}")
        print(f"[RULE ENGINE] Has explanation: {explanation is not None}")
        
        # Return structured format for easy frontend parsing
        return {
            'type': explanation['severity'],
            'line': line,
            'code': error_code,
            'severity': explanation['severity'],
            'structured': {
                'title': explanation['title'],
                'sections': [
                    {
                        'icon': '📋',
                        'heading': 'What\'s Wrong',
                        'content': explanation['explain'],
                        'type': 'explain'
                    },
                    {
                        'icon': '🔧',
                        'heading': 'How to Fix',
                        'content': explanation['how_to_fix'],
                        'type': 'fix'
                    },
                    {
                        'icon': '📝',
                        'heading': 'Examples',
                        'content': {
                            'wrong': explanation['wrong'],
                            'right': explanation['right']
                        },
                        'type': 'example'
                    },
                    {
                        'icon': '📚',
                        'heading': 'Learn More',
                        'content': explanation['learn'],
                        'type': 'learn'
                    }
                ]
            },
            # Legacy: Keep message field for backwards compatibility
            'message': self._format_legacy_message(explanation)
        }
    
    def _format_legacy_message(self, explanation):
        """
        Format explanation as string for backwards compatibility
        """
        message = f"{explanation['title']}\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        message += f"📋 WHAT'S WRONG:\n{explanation['explain']}\n\n"
        message += f"🔧 HOW TO FIX:\n{explanation['how_to_fix']}\n\n"
        message += f"📝 EXAMPLE:\n\n"
        message += f"❌ WRONG:\n{explanation['wrong']}\n\n"
        message += f"✅ RIGHT:\n{explanation['right']}\n\n"
        message += f"📚 LEARN MORE:\n{explanation['learn']}"
        return message
    
    def add_optimization_suggestions(self, code_lines):
        """
        Analyze code and provide optimization suggestions with structured format
        
        Args:
            code_lines: List of code lines
            
        Returns:
            List of structured optimization suggestions
        """
        suggestions = []
        code_str = '\n'.join(code_lines)
        
        for i, line in enumerate(code_lines, 1):
            line_stripped = line.strip()
            
        # Rule 1: List comprehension opportunity
            if 'for' in line_stripped and i < len(code_lines):
                next_line = code_lines[i].strip() if i < len(code_lines) else ""
                if '.append(' in next_line:
                    suggestions.append({
                        'line': i,
                        'title': '✨ List Comprehension Opportunity',
                        'explain': 'You can use a list comprehension here for cleaner, more Pythonic, and faster code.',
                        'how_to_fix': 'Replace the for-loop with a list comprehension.',
                        'wrong': 'result = []\nfor item in items:\n    result.append(item * 2)',
                        'right': 'result = [item * 2 for item in items]  # One line, cleaner!',
                        'learn': '💡 List comprehensions are not only more readable but also faster than manual append loops!',
                        'severity': 'optimization'
                    })
            
        # Rule 2: range(len()) pattern
            if 'range(len(' in line_stripped:
                suggestions.append({
                    'line': i,
                    'title': '💡 Use enumerate() Instead',
                    'explain': "Instead of range(len()), use enumerate() to get both index and value.",
                    'how_to_fix': 'Replace range(len(items)) with enumerate(items)',
                    'wrong': 'for i in range(len(items)):\n    print(i, items[i])',
                    'right': 'for i, item in enumerate(items):\n    print(i, item)  # Cleaner and Pythonic!',
                    'learn': '💡 enumerate() gives you both the index and value elegantly without indexing!',
                    'severity': 'optimization'
                })
            
        # Rule 3: String concatenation
            if '+=' in line_stripped and ('str' in line_stripped.lower() or '"' in line_stripped or "'" in line_stripped):
                suggestions.append({
                    'line': i,
                    'title': '🚀 Inefficient String Concatenation',
                    'explain': "You're building a string by repeatedly using += in a loop. This looks simple but it's actually very slow for large strings! Here's why: strings in Python are immutable (can't be changed). Every time you do += , Python creates a brand NEW string with all the old content plus the new part. It's like rewriting an entire book every time you want to add one word! This makes string concatenation O(n²) complexity - it gets exponentially slower with more additions.",
                    'how_to_fix': "Use str.join() for efficient string building:\n1. Collect all pieces in a list first\n2. Use ''.join(list) or ' '.join(list) to combine them all at once\n3. For small strings (< 10 concatenations), += is fine\n4. For many concatenations, join() can be 10x-100x faster\n5. Alternative: use f-strings or format() for single-line combinations",
                    'wrong': 'result = ""\nfor word in ["hello", "world", "python"]:\n    result += word + " "  # Creates 3 new strings!\n# Gets exponentially slower with more words',
                    'right': 'words = ["hello", "world", "python"]\nresult = " ".join(words)  # One operation!\n# OR for complex building:\nparts = []\nfor word in words:\n    parts.append(word)\nresult = " ".join(parts)',
                    'learn': '💡 Each += creates a completely new string by copying everything! It\'s like building a tower by rebuilding the entire thing from scratch every time you add a block. join() is like having all the blocks ready and stacking them once. For 1000 words, += does 500,000 copy operations, join() does 1000. That\'s the power of O(n) vs O(n²)!',
                    'severity': 'optimization'
                })
        
        # Rule 4: == True or == False (check only once, not per line)
        if '== True' in code_str or '== False' in code_str:
            if not any(s.get('title') == "🎯 Redundant Boolean Comparison" for s in suggestions):
                line_num = self._find_line('== True', code_lines) or self._find_line('== False', code_lines)
                suggestions.append({
                    'line': line_num,
                    'title': "🎯 Redundant Boolean Comparison",
                    'explain': "You're comparing a boolean value to True or False using ==. This is redundant because the value is ALREADY True or False! It's like asking 'Is this true thing equal to true?' - the answer is built into the question. This makes code longer, harder to read, and marks you as a beginner. Every Python developer recognizes this as a code smell.",
                    'how_to_fix': "Remove the comparison:\n1. For '== True': Just use the variable directly (if is_ready:)\n2. For '== False': Use 'not' keyword (if not is_ready:)\n3. This works because if statements already check for truthiness\n4. Same applies in while loops and other conditions",
                    'wrong': 'is_valid = True\nif is_valid == True:  # Redundant!\n    print("Valid")\n\nis_empty = False\nif is_empty == False:  # Redundant!\n    print("Not empty")\n\nwhile running == True:  # Redundant!\n    pass',
                    'right': 'is_valid = True\nif is_valid:  # Clean and Pythonic!\n    print("Valid")\n\nis_empty = False\nif not is_empty:  # Clean and Pythonic!\n    print("Not empty")\n\nwhile running:  # Clean and Pythonic!\n    pass',
                    'learn': '💡 Boolean values are designed to be used directly in conditions! Comparing them to True/False is like saying "Is this yes equal to yes?" If something is already True, you don\'t need to check if it equals True - it IS True! This is one of the most common beginner mistakes. Master this and your code instantly looks more professional.',
                    'severity': 'optimization'
                })
        
        # Rule 5: Mutable default arguments (check in current line only)
            if 'def ' in line_stripped and ('=[]' in line_stripped.replace(' ', '') or '={}' in line_stripped.replace(' ', '')):
                suggestions.append({
                    'line': i,
                    'title': "⚠️ Dangerous Mutable Default Argument",
                    'explain': "Using [] or {} as default argument is dangerous - the same object is shared between all function calls!",
                    'how_to_fix': "Use None as default, then create the list/dict inside the function.",
                    'wrong': 'def add_item(item, items=[]):  # Dangerous!\n    items.append(item)\n    return items',
                    'right': 'def add_item(item, items=None):  # Safe!\n    if items is None:\n        items = []\n    items.append(item)\n    return items',
                    'learn': '💡 Default mutable arguments are created once when the function is defined and reused forever! Like everyone sharing one shopping cart.',
                    'severity': 'optimization'
                })
        
        # Rule 6: File operations without 'with' (check only once)
        if 'open(' in code_str and 'with ' not in code_str:
            if not any(s.get('title') == "📁 File Not Using 'with' Statement" for s in suggestions):
                line_num = self._find_line('open(', code_lines)
                suggestions.append({
                    'line': line_num,
                    'title': "📁 File Operations Without 'with' Statement",
                    'explain': "You're opening a file without using a 'with' statement (context manager). This is risky because if an error occurs after opening the file but before closing it, the file stays open forever (file leak). Open files consume system resources and can prevent other programs from accessing them. Even if you have f.close(), it won't run if an exception happens first. It's like leaving your house without locking the door - might be fine, but why risk it?",
                    'how_to_fix': "Use 'with' statement for automatic cleanup:\n1. Replace: f = open('file.txt')\n2. With: with open('file.txt', encoding='utf-8') as f:\n3. Indent your file operations under the with block\n4. File automatically closes when block ends, even if errors occur\n5. Always specify encoding='utf-8' for text files",
                    'wrong': 'f = open("data.txt", "r")\ndata = f.read()\nf.close()  # Won\'t run if read() fails!\n\n# File leak risk:\nf = open("output.txt", "w")\nprocess_data(f)  # If this fails, file never closes!\nf.close()',
                    'right': 'with open("data.txt", "r", encoding="utf-8") as f:\n    data = f.read()  # Auto-closes even if error!\n\n# Safe file handling:\nwith open("output.txt", "w", encoding="utf-8") as f:\n    process_data(f)  # File closes automatically!',
                    'learn': '💡 The \'with\' statement is Python\'s automatic cleanup crew! It guarantees files close properly even when things go wrong. Think of it like automatic car locks - when you walk away, they lock automatically. You don\'t have to remember to close files, Python does it for you. This prevents resource leaks and is the professional Python way. Always use \'with\' for files, database connections, network sockets, etc.',
                    'severity': 'optimization'
                })
        
        # Rule 7: Using type() for type checking (check only once)
        if 'type(' in code_str and '==' in code_str:
            if not any(s.get('title') == "🔍 Use isinstance() for Type Checking" for s in suggestions):
                line_num = self._find_line('type(', code_lines)
                suggestions.append({
                    'line': line_num,
                    'title': "🔍 Use isinstance() Instead of type()",
                    'explain': "You're using type(x) == SomeType to check types. This works but has a critical flaw: it doesn't work with inheritance (subclasses)! If you have a subclass, type() will say it's NOT the parent class even though it is. It's like saying a sports car isn't a car because you're checking for the exact model. isinstance() is the proper, Pythonic way that respects inheritance and is what professional Python developers always use.",
                    'how_to_fix': "Replace type() comparisons with isinstance():\n1. Change: if type(value) == list:\n2. To: if isinstance(value, list):\n3. Works with inheritance (checks 'is this a kind of X?')\n4. More readable and Pythonic\n5. Can check multiple types: isinstance(value, (int, float))",
                    'wrong': 'value = [1, 2, 3]\nif type(value) == list:  # Works but not Pythonic\n    print("It\'s a list")\n\n# Breaks with inheritance:\nclass MyList(list):\n    pass\n\nmy_list = MyList([1, 2])\nif type(my_list) == list:  # False! Broken!\n    print("Never prints")',
                    'right': 'value = [1, 2, 3]\nif isinstance(value, list):  # Pythonic!\n    print("It\'s a list")\n\n# Works with inheritance:\nclass MyList(list):\n    pass\n\nmy_list = MyList([1, 2])\nif isinstance(my_list, list):  # True! Works!\n    print("Prints correctly")\n\n# Check multiple types:\nif isinstance(value, (int, float)):\n    print("It\'s a number")',
                    'learn': '💡 isinstance() is the professional way to check types in Python! It respects the object-oriented principle that a subclass IS its parent class. type() is like checking someone\'s ID card for their exact birthday when you just need to know if they\'re an adult. isinstance() asks the right question: "Is this thing a kind of what I\'m looking for?" Use it always!',
                    'severity': 'optimization'
                })
        
        # Rule 8: Global variable usage (check only once)
        if 'global ' in code_str:
            if not any(s.get('title') == "🌍 Avoid Global Variables" for s in suggestions):
                line_num = self._find_line('global ', code_lines)
                suggestions.append({
                    'line': line_num,
                    'title': "🌍 Avoid Global Variables",
                    'explain': "You're using the 'global' keyword to modify a variable from outside a function. While this works, it's considered bad practice in almost all cases. Global variables create 'hidden connections' between functions - changing one function can mysteriously break another. They make code impossible to test (you can't test a function in isolation), hard to debug (where did this value come from?), and difficult to understand (what changes this global?). It's like everyone in a building sharing one light switch - chaos!",
                    'how_to_fix': "Pass values as parameters, return results:\n1. Remove the 'global' statement\n2. Add the variable as a function parameter\n3. Return the new value from the function\n4. Assign the result: counter = increment(counter)\n5. For complex state, use classes instead",
                    'wrong': 'counter = 0  # Global state\n\ndef increment():\n    global counter  # Modifying global - BAD!\n    counter += 1\n\ndef reset():\n    global counter\n    counter = 0\n\n# Hard to test, hidden dependencies',
                    'right': '# Pass and return approach:\ndef increment(counter):\n    return counter + 1  # Pure function!\n\ndef reset():\n    return 0\n\n# Using it:\ncounter = 0\ncounter = increment(counter)\ncounter = reset()\n\n# OR use a class for related state:\nclass Counter:\n    def __init__(self):\n        self.value = 0\n    \n    def increment(self):\n        self.value += 1',
                    'learn': '💡 Functions should be like vending machines - you put something in (parameters), you get something out (return value). No hidden global state! Global variables are like having a shared bank account with strangers - you never know who\'s changing what. Pure functions (no global state) are easier to test, debug, and understand. If you need shared state, use classes or pass parameters. Your future self will thank you!',
                    'severity': 'optimization'
                })
        
        # Rule 9: Bare except clause (check only once)
        if 'except:' in code_str:
            if not any(s.get('title') == "🎭 Bare Except Clause" for s in suggestions):
                line_num = self._find_line('except:', code_lines)
                suggestions.append({
                    'line': line_num,
                    'title': "🎭 Dangerous Bare Except Clause",
                    'explain': "You're using a bare 'except:' which catches EVERY possible error - not just the ones you expect! This catches SystemExit (when Python tries to exit), KeyboardInterrupt (Ctrl+C), MemoryError, and even bugs in your code. This means: 1) You can't stop your program with Ctrl+C, 2) Real bugs get hidden, 3) System errors are silenced. It's like putting a safety net that catches everything including ambulances trying to help you!",
                    'how_to_fix': "Specify which exceptions to catch:\n1. Replace: except:\n2. With: except ValueError: or except (TypeError, ValueError):\n3. Only catch exceptions you expect and can handle\n4. Use 'except Exception as e:' if you must catch most errors\n5. Never catch SystemExit or KeyboardInterrupt",
                    'wrong': 'try:\n    value = int(input("Enter number: "))\n    result = 100 / value\nexcept:  # Catches EVERYTHING!\n    print("Error")  # What error? Who knows!\n\n# Can\'t stop with Ctrl+C:\nwhile True:\n    try:\n        risky_operation()\n    except:  # Traps you in infinite loop!\n        pass',
                    'right': 'try:\n    value = int(input("Enter number: "))\n    result = 100 / value\nexcept ValueError:\n    print("Please enter a valid number")\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")\n\n# Specific and helpful:\ntry:\n    risky_operation()\nexcept ConnectionError as e:\n    print(f"Network problem: {e}")\nexcept TimeoutError:\n    print("Operation timed out")',
                    'learn': '💡 Catch only the exceptions you expect and know how to handle! Bare except is like a doctor saying "you have a disease" but not which one - useless and scary! When you catch specific exceptions (ValueError, FileNotFoundError), your error messages can be helpful. Bare except hides bugs and makes debugging nightmare. Think of exception handling like a safety net with specific holes - you want to catch the falling apples, not the rescue helicopter!',
                    'severity': 'optimization'
                })
        
        # Convert all suggestions to structured format
        return [self._convert_optimization_to_structured(opt) for opt in suggestions]
    
    def _find_line(self, pattern, code_lines):
        """Helper to find line number containing pattern"""
        for i, line in enumerate(code_lines, 1):
            if pattern in line:
                return i
        return 1  # Default to line 1 if not found
    

    def _convert_optimization_to_structured(self, opt):
        """
        Convert old optimization format to new structured format
        Compatible with FeedbackItem model
        """
        return {
            'type': 'optimization',
            'line': opt['line'],
            'code': 'OPT-' + opt['title'][:20].replace(' ', '-'),  # Generate code like OPT-List-Comprehension
            'severity': 'optimization',
            'structured': {
                'title': opt['title'],
                'sections': [
                    {
                        'icon': '📋',
                        'heading': 'What\'s Wrong',
                        'content': opt['explain'],
                        'type': 'explain'
                    },
                    {
                        'icon': '🔧',
                        'heading': 'How to Fix',
                        'content': opt['how_to_fix'],
                        'type': 'fix'
                    },
                    {
                        'icon': '📝',
                        'heading': 'Examples',
                        'content': {
                            'wrong': opt['wrong'],
                            'right': opt['right']
                        },
                        'type': 'example'
                    },
                    {
                        'icon': '📚',
                        'heading': 'Learn More',
                        'content': opt['learn'],
                        'type': 'learn'
                    }
                ]
            },
            'message': self._format_optimization_message(opt)
        }
    
    def _format_optimization_message(self, opt):
        """Format optimization as legacy message string"""
        message = f"{opt['title']}\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        message += f"📋 WHAT'S WRONG:\n{opt['explain']}\n\n"
        message += f"🔧 HOW TO FIX:\n{opt['how_to_fix']}\n\n"
        message += f"📝 EXAMPLE:\n\n"
        message += f"❌ WRONG:\n{opt['wrong']}\n\n"
        message += f"✅ RIGHT:\n{opt['right']}\n\n"
        message += f"📚 LEARN MORE:\n{opt['learn']}"
        return message