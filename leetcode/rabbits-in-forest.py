class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        population = 0
        left_pointer = 0
        pointer = 1
        
        while pointer < len(answers):
            
            while pointer < len(answers) and pointer - left_pointer <= answers[left_pointer] and answers[pointer] == answers[left_pointer]:
                pointer += 1
                
            population += answers[left_pointer] + 1
            left_pointer = pointer
            
            
        return population