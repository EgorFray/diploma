import matplotlib.pyplot as plt
import numpy as np

d = float(input("Значення діаметра стеклопластикового стрижня: "))
pi = 3.14
LD = int(input("Лінійна щільність однієї нитки: "))  # 8750
p = 1.44
m = int(input("Кількість ниток : "))
Er = [0.05, 0.1, 0.2, 0.3, 0.4]
print("---------")


# Scc
def area_glass_tube():
    formula_for_glass_tube = round((pi * d**2)/4, 2)
    print("Площа стеклопластикового стрижня: " + str(formula_for_glass_tube))
    return formula_for_glass_tube


# Saн
def area_aramid_threads():
    formula_for_aramid_threads = round((LD/p) * m * 10**(-4), 2)
    print("Площа арамідних ниток: " + str(formula_for_aramid_threads))
    return formula_for_aramid_threads


list_of_g1 = []
# G1 при 20 градусов цельсия


def voltage_of_aramid_threads():
    for i in Er:
        formula_for_voltage_of_aramid_threads = i * 10**(-2) * 55000
        print("Напруга в арамідних нитках при Er = " + str(i) + ': ' + str(formula_for_voltage_of_aramid_threads))
        list_of_g1.append(formula_for_voltage_of_aramid_threads)
    return list_of_g1


# Eф
def fictive_module_of_bending():
    Scc = area_glass_tube()
    Saн = area_aramid_threads()
    formula_for_fictive_module_of_bending = round((Scc * 55000 + Saн * 104000) / (Scc + Saн), 1)
    print("Фіктивний модуль пружності СНОК: " + str(formula_for_fictive_module_of_bending))
    return formula_for_fictive_module_of_bending


# gx1 при - 40С
def fictive_voltage():
    Eф = fictive_module_of_bending()
    dT = 293 - int(input("Температура в кельвінах: "))
    for g in list_of_g1:
        list_of_voltages = []
        for i in range(4):
            formula_for_fictive_voltage = round((g - (-3 * 10**(-6) - (-0.19 * 10**(-6))) * dT * 104000) * Eф / 104000, 2)
            list_of_voltages.append(formula_for_fictive_voltage)
            dT -= 20
            print("gx" + str(i + 1) + ": " + str(formula_for_fictive_voltage))

        x = [-40, -20, 0, +20]
        plt.plot(x, list_of_voltages)
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_color('red')
        plt.show()
    return list_of_voltages


if __name__ == '__main__':
    area_glass_tube(),
    print("---------")
    area_aramid_threads(),
    print("---------")
    voltage_of_aramid_threads(),
    print("---------")
    fictive_module_of_bending(),
    print("---------")
    fictive_voltage(),
