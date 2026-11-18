def hasDuplicate(nums) -> bool:
        lista = set()

        for i in range(len(nums)):
            if nums[i] in lista:
                return True

            lista.add(nums[i])
        
        return False
