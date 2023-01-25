def compare_losses(data1, data2, label1, label2):
    """
    Function: compare_losses
    Description:
    Create a plot to visualize the loss data compiled by loss_analysis()
    For Google Colab an upgrade of matplotlib might be necessary (pip install matplotlib --upgrade)
    Parameters:
        - Logic (Object)
        - Group Leader(s) (Array)
    Optional:
        Logic Parameters (Must be passed associated with Object using "setVariable")
        - Location Type (String)
            setVariable ["attackLocType", value]
        - Attack Position (XYZ, Object, Location, Group, Marker, or Task)
            setVariable ["attackPosition", value]
        - Search Radius (Scalar)
            setVariable ["searchRadius", value]
        - Allow Override (Bool)
            setVariable ["allowOverride", value]
    Example:
        (begin example)
        [Logic, [group1 ,group2, ..., groupN]] call CBA_fnc_moduleAttack;
        (end)
    Returns:
        Nil
    Author:
        AK
    """
    import matplotlib.pyplot as plt
    import numpy as np

    def fill_datasets(dict1, dict2):
        for key in dict1.keys():
            if key not in dict2.keys():
                dict2[key] = 0

    def arrange_data_for_plot(dict1, dict2):
        x = []
        y = []
        category = []
        for key in dict1.keys():
            x.append(dict1[key])
            y.append(dict2[key])
            category.append(key)
        return (x, y, category)



    fill_datasets(data1, data2)
    fill_datasets(data2, data1)
    # un

    x_and_y = arrange_data_for_plot(data1, data2)

    labels = x_and_y[2] # ENHANCE this is very sloppy
    men_means = x_and_y[0]
    women_means = x_and_y[1]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label=label1)
    rects2 = ax.bar(x + width/2, women_means, width, label=label2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Losses')
    ax.set_title('Losses by Type and Nation')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()