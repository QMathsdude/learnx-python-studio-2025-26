from math import sqrt

G = 11506.1

def calc_single_grav(x_this, y_this, x_other, y_other, mass_other):
    x_rel = x_other - x_this
    y_rel = y_other - y_this

    dist = sqrt(x_rel * x_rel + y_rel * y_rel)
    x_norm = x_rel / dist
    y_norm = y_rel / dist

    g = G * mass_other / (dist * dist)
    return g * x_norm, g * y_norm

def calc_total_grav(xs, ys, idx, n, ms):
    ax_total = 0.
    ay_total = 0.
    x = xs[idx]
    y = ys[idx]
    for i in range(n):
        if i == idx:
            continue
        ax, ay = calc_single_grav(x, y, xs[i], ys[i], ms[i])
        ax_total += ax
        ay_total += ay
    return ax_total, ay_total

def nbody_sim(initials, steps, dt):
    num_bodies = len(initials)
    masses = [p[0] for p in initials]

    xhist = tuple([ p[1][0] ] for p in initials)
    yhist = tuple([ p[1][1] ] for p in initials)

    xs = [p[1][0] for p in initials]
    ys = [p[1][1] for p in initials]

    vxs = [p[2][0] for p in initials]
    vys = [p[2][1] for p in initials]

    axs = []
    ays = []
    for i in range(num_bodies):
        ax, ay = calc_total_grav(xs, ys, i, num_bodies, masses)
        axs.append(ax)
        ays.append(ay)

    for i in range(steps):
        # if i % 10_000 == 0:
        #     print(i)

        # First iter to update pos ONLY
        for j in range(num_bodies):
            xs[j] += vxs[j]*dt + 0.5*axs[j]*dt*dt
            ys[j] += vys[j]*dt + 0.5*ays[j]*dt*dt

        # Second iter to update vel and acc ONLY
        for j in range(num_bodies):
            ax_new, ay_new = calc_total_grav(xs, ys, j, num_bodies, masses)
            vxs[j] += 0.5 * (axs[j] + ax_new) * dt
            vys[j] += 0.5 * (ays[j] + ay_new) * dt
            axs[j] = ax_new
            ays[j] = ay_new

        for j in range(num_bodies):
            xhist[j].append(xs[j])
            yhist[j].append(ys[j])

    return xhist, yhist