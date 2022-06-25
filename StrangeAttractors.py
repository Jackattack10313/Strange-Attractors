import plotly.express as px
import pandas as pd


# Approximates the solutions to the differential equations in phase space
def displayLorenzAttractor():
    try:
        timeStep = float(eval(input("Enter the time step for each iteration (I recommend <0.001s): ")))
        sigma = float(eval(input("Enter the value for sigma (Lorenz used 10): ")))
        beta = float(eval(input("Enter the value for beta (Lorenz used 8/3): ")))
        rho = float(eval(input("Enter the value for rho (Lorenz used 28): ")))
        xInitial = float(input("Enter the initial rate of convection - x: "))
        yInitial = float(input("Enter the initial horizontal temperature variation - y: "))
        zInitial = float(input("Enter the vertical temperature variation - z: "))
        iterations = int(input("Enter the number of iterations: "))
        x = [xInitial]
        y = [yInitial]
        z = [zInitial]
        time = [0]
        for i in range(iterations):
            x.append((sigma * (y[i] - x[i])) * timeStep + x[i])
            y.append((x[i] * (rho - z[i]) - y[i]) * timeStep + y[i])
            z.append((x[i] * y[i] - beta * z[i]) * timeStep + z[i])
            time.append(time[i] + timeStep)
        df = pd.DataFrame(
            {"Convection Rate": x, "Horizontal Temperature Variation": y, "Vertical Temperature Variation": z,
             "time": time})
        fig = px.scatter_3d(df, x="Convection Rate", y="Horizontal Temperature Variation", z="Vertical Temperature "
                                                                                             "Variation", color="time")
        fig.show()
    except BaseException:
        print("Invalid input")


# Meant to show how points that start close together diverge quickly
def twoPointsLorenzAttractor():
    try:
        timeStep = float(eval(input("Enter the time step for each iteration (I recommend <0.001s): ")))
        sigma = float(eval(input("Enter the value for sigma (Lorenz used 10): ")))
        beta = float(eval(input("Enter the value for beta (Lorenz used 8/3): ")))
        rho = float(eval(input("Enter the value for rho (Lorenz used 28): ")))
        x1Initial = float(input("Enter the initial rate of convection for the first point - x: "))
        y1Initial = float(input("Enter the initial horizontal temperature variation for the first point - y: "))
        z1Initial = float(input("Enter the vertical temperature variation for the first point - z: "))
        x2Initial = float(input("Enter the initial rate of convection for the second point - x: "))
        y2Initial = float(input("Enter the initial horizontal temperature variation for the second point - y: "))
        z2Initial = float(input("Enter the vertical temperature variation for the second point- z: "))
        iterations = int(
            input("Enter the number of iterations (Try to keep around 1000 - otherwise the browser freezes): "))
        x1 = [x1Initial]
        y1 = [y1Initial]
        z1 = [z1Initial]
        x2 = [x2Initial]
        y2 = [y2Initial]
        z2 = [z2Initial]
        group1 = ["point 1"]
        group2 = ["point 2"]
        time = [0]
        for i in range(iterations):
            x1.append((sigma * (y1[i] - x1[i])) * timeStep + x1[i])
            y1.append((x1[i] * (rho - z1[i]) - y1[i]) * timeStep + y1[i])
            z1.append((x1[i] * y1[i] - beta * z1[i]) * timeStep + z1[i])
            x2.append((sigma * (y2[i] - x2[i])) * timeStep + x2[i])
            y2.append((x2[i] * (rho - z2[i]) - y2[i]) * timeStep + y2[i])
            z2.append((x2[i] * y2[i] - beta * z2[i]) * timeStep + z2[i])
            time.append(time[i] + timeStep)
            group1.append("point 1")
            group2.append("point 2")
        x = x1 + x2
        y = y1 + y2
        z = z1 + z2
        time += time
        group = group1 + group2
        df = pd.DataFrame(
            {"Convection Rate": x, "Horizontal Temperature Variation": y, "Vertical Temperature Variation": z,
             "time": time, "group": group})
        fig = px.scatter_3d(df, x="Convection Rate", y="Horizontal Temperature Variation", z="Vertical Temperature "
                            "Variation", animation_frame="time", animation_group="group", color="group")
        fig.update_layout(scene=dict(
            xaxis=dict(range=[-max(x) * 1.5, max(x) * 1.5], ),
            yaxis=dict(range=[-max(y) * 1.5, max(y) * 1.5], ),
            zaxis=dict(range=[-max(z) * 1.5, max(z) * 1.5], ), ),
        )
        fig.show()
    except BaseException:
        print("Invalid input")


# Approximates the solutions to the differential equations in phase space
def displayRosslerAttractor():
    try:
        timeStep = float(eval(input("Enter the time step for each iteration (I recommend <0.001s): ")))
        a = float(eval(input("Enter the value for a (Rössler used 0.2): ")))
        b = float(eval(input("Enter the value for b (Rössler used 0.2): ")))
        c = float(eval(input("Enter the value for c (Rössler used 5.7): ")))
        xInitial = float(input("Enter the initial x: "))
        yInitial = float(input("Enter the initial y: "))
        zInitial = float(input("Enter the vertical z: "))
        iterations = int(input("Enter the number of iterations: "))
        x = [xInitial]
        y = [yInitial]
        z = [zInitial]
        time = [0]
        for i in range(iterations):
            x.append((-y[i] - z[i]) * timeStep + x[i])
            y.append((x[i] + a * y[i]) * timeStep + y[i])
            z.append((b + z[i] * (x[i] - c)) * timeStep + z[i])
            time.append(time[i] + timeStep)
        df = pd.DataFrame({"x": x, "y": y, "z": z,
                           "time": time})
        fig = px.scatter_3d(df, x="x", y="y", z="z",
                            color="time")
        fig.show()
    except BaseException():
        print("Invalid input")


# Meant to show how points that start close together diverge quickly
def twoPointsRosslerAttractor():
    try:
        timeStep = float(eval(input("Enter the time step for each iteration (I recommend <0.001s): ")))
        a = float(eval(input("Enter the value for a (Rössler used 0.2): ")))
        b = float(eval(input("Enter the value for b (Rössler used 0.2): ")))
        c = float(eval(input("Enter the value for c (Rössler used 5.7): ")))
        x1Initial = float(input("Enter the initial x: "))
        y1Initial = float(input("Enter the initial y: "))
        z1Initial = float(input("Enter the vertical z: "))
        x2Initial = float(input("Enter the initial x: "))
        y2Initial = float(input("Enter the initial y: "))
        z2Initial = float(input("Enter the vertical z: "))
        iterations = int(input("Enter the number of iterations (Try to keep around 1000 - otherwise the browser "
                               "freezes): "))
        x1 = [x1Initial]
        y1 = [y1Initial]
        z1 = [z1Initial]
        x2 = [x2Initial]
        y2 = [y2Initial]
        z2 = [z2Initial]
        group1 = ["point1"]
        group2 = ["point2"]
        time = [0]
        for i in range(iterations):
            x1.append((-y1[i] - z1[i]) * timeStep + x1[i])
            y1.append((x1[i] + a * y1[i]) * timeStep + y1[i])
            z1.append((b + z1[i] * (x1[i] - c)) * timeStep + z1[i])
            x2.append((-y2[i] - z2[i]) * timeStep + x2[i])
            y2.append((x2[i] + a * y2[i]) * timeStep + y2[i])
            z2.append((b + z2[i] * (x2[i] - c)) * timeStep + z2[i])
            time.append(time[i] + timeStep)
            group1.append("point 1")
            group2.append("point 2")
        x = x1 + x2
        y = y1 + y2
        z = z1 + z2
        time += time
        group = group1 + group2
        df = pd.DataFrame({"x": x, "y": y, "z": z,
                           "time": time, "group": group})
        fig = px.scatter_3d(df, x="x", y="y", z="z",
                            animation_frame="time", animation_group="group", color="group")
        fig.update_layout(scene=dict(
            xaxis=dict(range=[-max(x) * 1.5, max(x) * 1.5], ),
            yaxis=dict(range=[-max(y) * 1.5, max(y) * 1.5], ),
            zaxis=dict(range=[-max(z) * 1.5, max(z) * 1.5], ), ),
        )
        fig.show()
    except BaseException:
        print("Invalid input")


def Menu():
    done = False
    while not done:
        try:
            print("Choose from the following:")
            print("1 - Lorenz Attractor")
            print("2 - 2 points on Lorenz Attractor (shows diverging points with very close starting positions)")
            print("3 - Rössler Attractor")
            print("4 - 2 points on Rössler Attractor (shows diverging points with very close starting positions)")
            selection = int(input("Selection: "))
            if 0 < selection < 5:
                if selection == 1:
                    displayLorenzAttractor()
                elif selection == 2:
                    twoPointsLorenzAttractor()
                elif selection == 3:
                    displayRosslerAttractor()
                else:
                    twoPointsRosslerAttractor()
        except BaseException:
            print("Invalid input")
        if input("Continue? [Y/n]: ").lower() != "y":
            done = True


if __name__ == "__main__":
    Menu()
