class solution:
    def subsets(self, set_element):
        return self.subsetsRecur([], sorted(set_element))
    
    def subsetsRecur(self, current, set_element):
        if set_element:
            return self.subsetsRecur(current, set_element[1:]) + self.subsetsRecur(current + [set_element[0]], set_element[1:])
        return [current]

print(solution().subsets([4,5,6]))