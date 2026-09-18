class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total_objects = len(nums)
        unique_numbers = set(nums)
        final_new_list = sorted(list(unique_numbers))
        acceptable_number = len(final_new_list) 
        #for i in range(acceptable_number):
            #if i < acceptable_number:
                #nums[i] = final_new_list[i]
        nums[:acceptable_number] = [final_new_list[i] for i in range(acceptable_number)]
        return acceptable_number
            
