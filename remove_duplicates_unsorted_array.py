5 2 4
  p  

s=(5,2,4)


if(heas is None):
	return head

p=head
s=set()
s.add(head.data)

while(p.next):
	if(p.next.data in s):
		p.next=p.next.next
	else:
		s.add(p.next.data)
		p=p.next
return head


-