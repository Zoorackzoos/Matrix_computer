"""
Consider the chemical reaction
aP4o10 + bCaF2 -> cPF5 + dCa3(PO4)2
Where a, b, c, and d are unknown positive integers. The reaction must be balanced; that is, the number of atoms of each element must be the same before and after the reaction. For example, because the number of oxygen atoms must remain the same,
10a = 8d
While there are many possible choices for a, b, c, and d that balance the reaction, it is customary to use the smallest possible integers. Balance this reaction.

A = _
B = _
C = _
D = _

a(P4O10) + b(CaF2) -> c(PF5) + d(Ca3(PO4)2)
aP4O10 = cPF5 + dCa3PO8 + bCaF2
aO10 = cF5/P3 + dCa3O8/P3 + bCaF2/P4
a = cF5/P3O10 + dCa3/P3O2 + bCaF2/P4O10

10a = 8d
10(cF5/P3O10 + dCa3/P3O2 + bCaF2/P4O10) = 8d
	STOP
	DO  NOT DO THIS

a(P4O10) + b(CaF2) -> c(PF5) + d(Ca3(PO4)2)
	P on the left = 4
	P on the right = 1 + 2
		4a = c + 2d
	O on the left = 10
	O on the right = 8
		10a = 8d
	Ca on the left = 1
	Ca on the right = 3
		1b = 3d
	F on the left = 2
	F on the right = 5
		2b = 5c

4a = c + 2d
10a = 8d
1b = 3d
2b = 5c
"""

def q_1_3_3(a_input, b_input, c_input, d_input, tab_amount="\t"):
    print(tab_amount,"q_1_3_3")
    tab_amount += "\t"
    print(tab_amount, "4(", "a", ") = ", "c", " + 2", "d")
    print(tab_amount, "10", "a", " = 8", 'd')
    print(tab_amount, "1", "b", " = 3", "d")
    print(tab_amount, "2", "b", " = 5", "c")
    print()
    print(tab_amount,"4(",a_input,") = ",c_input," + 2",d_input)
    print(tab_amount,"10",a_input," = 8",d_input)
    print(tab_amount,"1",b_input," = 3",d_input)
    print(tab_amount,"2",b_input," = 5",c_input)
    print()
    print(tab_amount, 4*a_input, " = ", c_input, " + ",d_input*2)
    print(tab_amount, 10*a_input, " = ", 8*d_input)
    print(tab_amount, b_input, " = ", 3*d_input)
    print(tab_amount, 2*b_input, " = ", 5*c_input)
    print()
    print(tab_amount, 4 * a_input, " = ", c_input + d_input * 2)
    print(tab_amount, 10 * a_input, " = ", 8 * d_input)
    print(tab_amount, b_input, " = ", 3 * d_input)
    print(tab_amount, 2 * b_input, " = ", 5 * c_input)

if __name__ == "__main__":
    #q_1_3_3(8,30,12,10,"\t")
    q_1_3_3(4, 15, 6, 5, "\t")
    #q_1_3_3(2, 15/2, 3, 5/2, "\t")


