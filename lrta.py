def neighbors(state, forbidden_states):
	feas_states=[]
	if state[0]>0 and [state[0]-1, state[1]] not in forbidden_states:
		feas_states.append([state[0]-1, state[1]]) 	#up
	if state[0]<9 and [state[0]+1, state[1]] not in forbidden_states:
		feas_states.append([state[0]+1, state[1]]) 	#down
	if state[1]>0 and [state[0], state[1]-1] not in forbidden_states:
		feas_states.append([state[0], state[1]-1]) 	#lft
	if state[1]<9 and [state[0], state[1]+1] not in forbidden_states:
		feas_states.append([state[0], state[1]+1]) 	#rgt
	return feas_states

def minimum_h(list_states, map_h):
	min_h=100
	min_h_state= 0
	for el in list_states:
		if map_h[el[0], el[1]]<min_h:
			min_h_state=el
			min_h=map_h[el[0], el[1]]
	return min_h_state, min_h


def lrta_search(map_h,map_d, start, target, forbidden_states):
	inner=[]
	last_n_h=10
	frontier=[start]
	while True:
		if len(frontier)==0:
			break
		else:
			n, _= minimum_h(frontier, map_h)#+map_d)
			new_h= map_h[n[0], n[1]]
			if len(inner)>0:
				jj= inner[-1]
				last_n_h= map_h[jj[0], jj[1]]
			else: 
				last_n_h=100
			if new_h<last_n_h:
				#print(frontier)
				frontier.remove(n)
				inner.append(n)
				for m in neighbors(n, forbidden_states):
					if inner.count(m)==0:
						frontier.append(m)
						map_d[m[0], m[1]]= min(map_d[m[0], m[1]], map_d[n[0], n[1]]+1)
					elif inner.count(m)>0 and (map_d[m[0], m[1]]> map_d[n[0], n[1]]+1):
						inner.remove(m)
						frontier.append(m)
						map_d[m[0], m[1]]=  map_d[n[0], n[1]]+1
			else:
				"""
				min_temp=100
				for el in reversed(inner):
					_ , min_son_h= minimum_h(neighbors(el, forbidden_states), map_h)
					map_h[el[0], el[1]]= min_son_h+1
					if min_temp> min_son_h+1:
						min_temp=min_son_h+1
				last_n_h= min_temp
				"""
				frontier.remove(n)
				r= inner.pop()
				_ , min_son_h= minimum_h(neighbors(r, forbidden_states), map_h)
				map_h[r[0], r[1]]= min_son_h+1
				frontier.append(r)
				print map_h
	return inner

