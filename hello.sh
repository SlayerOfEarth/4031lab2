#!/bin/bash
#string array
user_list=("user1" "user2" "user3")

#output for loop
for user in "${user_list[@]}"; do
	echo "$user"
done

a=2
b=2
c=$((a+b))

echo "bash says hello world"
echo "$a+$b=$c"
