import sympy as sp

def q_6_1_7_true():
    # Define symbols
    lam = sp.symbols('lambda')

    # Define matrix A
    A = sp.Matrix([
        [10, -5, 19],
        [-1, 6, -11],
        [-5, 5, -14]
    ])

    print("Matrix A:")
    sp.pprint(A)
    print("\n" + "="*50)

    # Step 1: Compute A - λI
    I = sp.eye(3)
    A_lam = A - lam * I

    print("\nA - λI:")
    sp.pprint(A_lam)
    print("\n" + "="*50)

    # Step 2: Determinant (characteristic polynomial)
    print("\nDeterminant det(A - λI):")
    det_expr = sp.expand(A_lam.det())
    sp.pprint(det_expr)

    print("\nFactored form:")
    factored = sp.factor(det_expr)
    sp.pprint(factored)

    # Step 3: Solve for eigenvalues
    eigenvalues = sp.solve(det_expr, lam)
    eigenvalues = sorted(eigenvalues)

    print("\nEigenvalues (sorted):")
    print(eigenvalues)

    print("\n" + "="*50)

    # Step 4: Eigenvectors
    for eig in eigenvalues:
        print(f"\n--- Solving for λ = {eig} ---")

        A_eig = A - eig * I
        print("\nA - λI:")
        sp.pprint(A_eig)

        print("\nRow-reduced form:")
        rref_matrix, pivots = A_eig.rref()
        sp.pprint(rref_matrix)

        print("\nSolving (A - λI)v = 0 ...")

        # Solve system
        x, y, z = sp.symbols('x y z')
        v = sp.Matrix([x, y, z])

        equations = A_eig * v
        sol = sp.linsolve((A_eig, sp.Matrix([0, 0, 0])), (x, y, z))

        print("\nGeneral solution:")
        print(sol)

        # Extract a nice eigenvector
        sol_list = list(sol)[0]
        vec = sp.Matrix(sol_list)

        # Pick a simple value for free variable
        free_syms = vec.free_symbols
        if free_syms:
            t = list(free_syms)[0]
            vec = vec.subs(t, 1)

        print("\nEigenvector (example):")
        sp.pprint(vec)

        print("\nVerification A*v and λ*v:")
        sp.pprint(A * vec)
        print("vs")
        sp.pprint(eig * vec)

        print("\n" + "-"*50)

if __name__ == "__main__":
    q_6_1_7_true()