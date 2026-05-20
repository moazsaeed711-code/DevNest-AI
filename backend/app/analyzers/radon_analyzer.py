from radon.complexity import cc_visit, average_complexity # cyclomatic complecity, average_complexity # Average complexity
from radon.metrics import mi_visit  # Maintainability Index

class RadonAnalyzer:
    def analyze(self, code):
        try:
            cc_results = cc_visit(code) # Counts decision points

            avg_complexity = average_complexity(cc_results) if cc_results else 1
            mi_score = mi_visit(code, multi=True)
            score = self._calculate_grade(avg_complexity, mi_score)
            
            return {
                'score': score,
                'cyclomatic': round(avg_complexity, 1),
                'maintainability': round(mi_score, 1)
            }
        
        except:
            return {
                'score': 'A',
                'cyclomatic': 1.0,
                'maintainability': 100.0
            }
    
    def _calculate_grade(self, complexity, maintainability):
        if complexity <= 5 and maintainability >= 80:
            return 'A'
        elif complexity <= 10 and maintainability >= 60:
            return 'B'
        elif complexity <= 20 and maintainability >= 40:
            return 'C'
        elif complexity <= 30 and maintainability >= 20:
            return 'D'
        else:
            return 'F'