class Solution {
    public int longestConsecutive(int[] nums) {

        HashSet<Integer>set=new HashSet<>();
        int temp =1;
        int counter=1;
        int maxcounter=1;

        if(nums.length==0){
            return 0;
        }

        for(int i =0;i<nums.length;i++){
            set.add(nums[i]);

        }

        for(int i =0;i<nums.length;i++){
            if(!(set.contains(nums[i]-1))){
                while(set.contains(nums[i]+temp)){
                    temp++;
                    counter++;
                    if(counter>=maxcounter){
                        maxcounter=counter;
                    }
                }
             }
counter=1;
temp=1;
        }

        return maxcounter;
            }
        }
