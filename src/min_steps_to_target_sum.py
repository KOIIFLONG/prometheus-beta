from typing import List

def min_steps_to_target_sum(numbers: List[int], target: int) -> int:
    """
    Calculate the minimum number of steps to reach the target sum using each number once.
    
    Args:
        numbers (List[int]): List of integers to use in calculations
        target (int): Target sum to reach
    
    Returns:
        int: Minimum number of steps to reach the target sum, or -1 if impossible
    """
    def backtrack(current_sum: int, index: int, steps: int, used: set) -> int:
        # Base case: if target is reached
        if current_sum == target:
            return steps
        
        # If we've gone through all numbers or steps are excessive
        if index >= len(numbers):
            return float('inf')
        
        # Try multiple options with the current number
        min_steps = float('inf')
        
        # Option 1: Add the current number
        if index not in used:
            new_used = used.copy()
            new_used.add(index)
            add_steps = backtrack(current_sum + numbers[index], index + 1, steps + 1, new_used)
            min_steps = min(min_steps, add_steps)
        
        # Option 2: Subtract the current number
        if index not in used:
            new_used = used.copy()
            new_used.add(index)
            sub_steps = backtrack(current_sum - numbers[index], index + 1, steps + 1, new_used)
            min_steps = min(min_steps, sub_steps)
        
        # Option 3: Skip the current number
        skip_steps = backtrack(current_sum, index + 1, steps, used)
        min_steps = min(min_steps, skip_steps)
        
        return min_steps
    
    # If numbers list is empty, impossible to reach target
    if not numbers:
        return -1
    
    result = backtrack(0, 0, 0, set())
    
    # Return -1 if no solution found
    return result if result != float('inf') else -1