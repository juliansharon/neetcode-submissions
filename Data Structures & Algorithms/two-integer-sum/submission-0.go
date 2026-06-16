func twoSum(nums []int, target int) []int {

    diffrenceMap:= map[int]int{}


    for i,num:= range nums{
        if val, ok := diffrenceMap[num]; ok{
            return []int{val,i}
        }
        diffrenceMap[target-num]= i

    }

    return []int{}

    
}
