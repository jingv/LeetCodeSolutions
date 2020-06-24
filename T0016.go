package main

import (
	"fmt";
	"sort";
	"math";
)

// For Sort
type IntList []int
	
func (a IntList) Len() int           { return len(a) }
func (a IntList) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a IntList) Less(i, j int) bool { return a[i] < a[j] }

func threeSumClosest(nums []int, target int) int {
	if len(nums) < 3{
		// Cannot Return nil as type int
		return 0
	}
	// Sort nums
	sort.Sort(IntList(nums))
	var result = nums[0] + nums[1] + nums[2]
	for index := range nums{
		//fmt.Println("index = ", index)
		// Index Error
		if index == len(nums) - 2{
			break
		}
		var left = index + 1
		var right = len(nums) - 1
		for{
			//fmt.Println("Left = ", left, ", Right = ", right)
			var item_sum = nums[index] + nums[left] + nums[right]
			if item_sum < target{
				left++
				//fmt.Println("Left = ", left)
				for{
					if left == right || nums[left] != nums[left - 1]{ 
						break 
					}
					//fmt.Println("Left = ", left)
					left++
				}
			} else if item_sum > target{
				right--
				//fmt.Println(", Right = ", right)
				for{
					if left == right || nums[right] != nums[right + 1]{ 
						break 
					}
					//fmt.Println(", Right = ", right)
					right--
				}
			} else {
				return item_sum
			}
			if math.Abs(float64(item_sum - target)) < math.Abs(float64(result - target)){
				result = item_sum
			}
			if left >= right{
				break
			}
		}		
	}
	return result
}

func main(){
	var tests = [][2][]int{
		{{1}, {1}},
		{{-1, 2, 1, -4}, {1}},
		{{-1, 2, 400}, {1}},
	}
	for _, item := range tests {
		// fmt.Println(item[0])
		// fmt.Println(item[1][0])
		fmt.Println(threeSumClosest(item[0], item[1][0]))
	}
}