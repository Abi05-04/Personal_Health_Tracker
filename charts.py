import matplotlib.pyplot as plt

def weight_chart(entries):
    dates = [e[1] for e in entries]
    weights = [e[2] for e in entries]

    plt.figure()
    plt.plot(dates, weights, marker='o')
    plt.title("Weight Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def steps_chart(entries):
    dates = [e[1] for e in entries]
    steps = [e[4] for e in entries]

    plt.figure()
    plt.bar(dates, steps)
    plt.title("Daily Steps")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()