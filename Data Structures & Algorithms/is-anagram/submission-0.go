func isAnagram(s string, t string) bool {
    checker := map[byte]int{}

    if len(s)!=len(t){
        return false
    }

    for _, char:= range s{
        checker[byte(char)]++
    }

    for _, char:= range t{
        checker[byte(char)]--
    }

    for _,v:=range checker{
        if v != 0{
            return false
        }
    }
    return true


}
