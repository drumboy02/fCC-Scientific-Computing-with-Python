def arithmetic_arranger(problems, show_answers=False):
    fvals, oper, svals, ans = [], [], [], []
    lines = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."

        vals = problem.split()
        for v in vals:
            if '+' in v or '-' in v:
                continue
            if not v.isdigit():
                return 'Error: Numbers must only contain digits.'
            if len(v) > 4:
                return 'Error: Numbers cannot be more than four digits.'

        fvals.append(vals[0])
        svals.append(vals[2])

        flen = len(fvals)
        slen = len(svals)
        oper.append(vals[1])
        if show_answers:
            ans.append(str(eval(problem)))
    # print(fvals)
    # print(oper)
    # print(svals)
    # print(ans)
    for v in range(0, flen):
        fvlen = len(fvals[v])
        svlen = len(svals[v])
        line = '--'
        fspace = '  '
        sspace = oper[v] + ' '

        if fvlen > svlen:
            fdif = ' ' * (fvlen - svlen)
            # print('fvlen', fvlen, 'fdif', fdif)
            if fvlen == 4:
                line += ('-' * fvlen)
                fvals[v] = fspace + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + fdif + svals[v]
                # print(svals[v])
            if fvlen == 3:
                line += ('-' * fvlen)
                fvals[v] = fspace + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + fdif + svals[v]
                # print(svals[v])
            if fvlen == 2:
                line += ('-' * fvlen)
                fvals[v] = fspace + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + fdif + svals[v]
                # print(svals[v])
            if fvlen == 1:
                line += ('-' * fvlen)
                fvals[v] = fspace + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + fdif + svals[v]
                # print(svals[v])

        if svlen > fvlen:
            sdif = ' ' * (svlen - fvlen)
            # print('svlen', svlen, 'sdif', sdif)
            if svlen == 4:
                line += ('-' * svlen)
                fvals[v] = fspace + sdif + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + svals[v]
                # print(svals[v])
            if svlen == 3:
                line += ('-' * svlen)
                fvals[v] = fspace + sdif + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + svals[v]
                # print(svals[v])
            if svlen == 2:
                line += ('-' * svlen)
                fvals[v] = fspace + sdif + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + svals[v]
                # print(svals[v])
            if svlen == 1:
                line += ('-' * svlen)
                fvals[v] = fspace + sdif + fvals[v]
                # print(fvals[v])
                svals[v] = sspace + svals[v]
                # print(svals[v])

        if fvlen == svlen:
            # print('equal len', fvlen)
            fspace + (' ' * fvlen)
            fvals[v] = fspace + fvals[v]
            sspace + (' ' * svlen)
            svals[v] = sspace + svals[v]
            line += ('-' * fvlen)
            # print(fvals[v])
            # print(svals[v])

        lines.append(line)
        if show_answers:
            lspace = len(line) - len(ans[v])
            ans[v] = ' ' * lspace + ans[v]
    fstr = '    '.join(fvals)
    # print(fstr)
    sstr = '    '.join(svals)
    # print(sstr)
    lstr = '    '.join(lines)
    # print(lstr)
    res = '    '.join(ans)
    # print(res)
    if show_answers:
        return fstr + '\n' + sstr + '\n' + lstr + '\n' + res
    else:
        return fstr + '\n' + sstr + '\n' + lstr


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))

