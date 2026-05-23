class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i in operations:
            if i.lstrip('-').isdigit():
                record.append(int(i))
            elif i == "+":
                record.append(record[-1] + record[-2])
            elif i=="D":
                record.append(record[-1]*2)
            elif i=="C":
                record.pop()
        return sum(record)

