import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import stats
import re
import os


def plot_approx(X_data, Y_data, input_function, plot_name='plot_name', plot_title='plot_title', x_label='x_label', y_label='y_label', Y_absolute_sigma = 0, scientific_view = True, print_cross = True, save_as_csv = False, to_latex = False, save_fig=True): 


    X_data = np.array(X_data)
    Y_data = np.array(Y_data)

    num_of_datasets = np.shape(X_data)[0]

    # преобразования функции к виду для питона

    fun_ex = {'linear':'a0*x+a1', 'poly_2':'a0*x**2+a1*x+a2', 'poly_3':'a0*x**3+a1*x**2+a2*x+a3','exp':'e^(a0*x+a1)+a2', 'ln':'ln(a0*x+a1)+a2'}
    
    inp = input_function

    try:
        inp = fun_ex[inp]
        fun = fun_ex[inp]
    except KeyError:
        fun = inp.replace('e', 'np.e')
        fun = fun.replace('^', '**')
        fun = fun.replace('log', 'np.log10')
        fun = fun.replace('ln', 'np.log')


    # пропишем функции
    num_coef = len(re.findall('a[0-9]', fun))

    approx1 = lambda x,a0: eval(fun)
    approx2 = lambda x,a0,a1: eval(fun)
    approx3 = lambda x,a0,a1,a2: eval(fun)
    approx4 = lambda x,a0,a1,a2,a3: eval(fun)
    approx5 = lambda x,a0,a1,a2,a3,a4: eval(fun)
    approx6 = lambda x,a0,a1,a2,a3,a4,a5: eval(fun)

    approx = eval('approx'+'{}'.format(num_coef))

    # используем функцию curve_fit
    opt = np.zeros((num_of_datasets,num_coef))
    cov = np.zeros((num_of_datasets,num_coef,num_coef))
    for i in range(num_of_datasets):
        opt[i], cov[i] = curve_fit(approx, X_data[i], Y_data[i], absolute_sigma = Y_absolute_sigma)


    # коэффициенты
    a = opt

    #получим погрешности для коэффициентов
    sigma_a = np.zeros((num_of_datasets,num_coef))
    for i in range(num_of_datasets):
        sigma_a[i] = np.diag(cov[i])

    # относистельные погрешности на коэффиценты
    rel_sigma_a = 100* sigma_a/abs(a)

    # подсчитаем стандартную ошибку аппроксимации
    S_e = []
    for i in range(num_of_datasets):
        residuals1 = Y_data[i] - approx(X_data[i],*opt[i])
        fres1 = sum(residuals1**2)
        S_e.append(np.sqrt(fres1/len(X_data[i])))


    # в легенду запишем функцию аппроксимации с определнными коэффициентами
    if scientific_view == True:
        tr1 = re.sub(r'a[0-9]', '{:.3E}', inp)
    else:
        tr1 = re.sub(r'a[0-9]', '{%.3f}', inp)
    tr = inp.replace('ln', '\ln ')
    tr1 = tr1.replace('e^', 'exp')
    tr1 = tr1.replace('**', '^')
    tr1 = tr1.replace('*', ' \cdot ')

    tr1 = '$ y(x) = ' + tr1 + '$'
    # выстроим верный порядок коэффициентов
    order = re.findall('a([0-9])', fun)
    a_ord = [0 for i in range(num_of_datasets)]
    for i in range(num_of_datasets):
        a_ord[i] = dict(zip(order, a[i]))
        a_ord[i] = dict(sorted(a_ord[i].items()))
        a_ord[i] = tuple(a_ord[i].values())

    # это легенда в графике
    if scientific_view == True:
        leg = []
        for i in range(num_of_datasets):
            leg.append(tr1.format(*a_ord[i]))
    else:
        leg = []
        for i in range(num_of_datasets):
            leg.append(tr1%a_ord[i])




    # график
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')

    for i in range(num_of_datasets):
        # определяем массив точек по оси Ох и строим график аппроксимации
        dots = np.arange(X_data[i][0], max(X_data[i]) + 0.0001, 0.01)
        ax.plot(dots, approx(dots, *opt[i]), '--', lw = 2, label = leg[i])

        # это строит "точками" твои начальные данные
        ax.scatter(X_data[i], Y_data[i], s = 15)

    plt.legend() 

    # название графика и подписи к осям
    ax.set_title(plot_title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    # это создает сетку и делает маркеры на осях
    ax.minorticks_on()
    ax.grid(which='minor', color = 'gray', linestyle = ':', linewidth = 0.5)
    ax.grid(which='major', linewidth = 0.5)

    # это кресты погрещности, но только вдоль оси Y
    if print_cross == True:
        for i in range(num_of_datasets):
            plt.errorbar(X_data[i], Y_data[i], fmt = 'ro', markersize = '4', yerr = S_e[i], capsize = 2, elinewidth = 1, capthick = 1, ecolor = 'black')

    # сохраним график в картинку?
    if save_fig == True:
        if os.path.exists('pictures'):
            plt.savefig('pictures/'+plot_name+'.png', dpi=400)
        else: 
            os.mkdir('pictures')
            plt.savefig('pictures/'+plot_name+'.png', dpi=400)


    # вывод коэффициентов и погрешностей
    pd.set_option('display.float_format', lambda x: '{:.3E}'.format(x))
    # названия коэффициентов в порядке ввода их в начале
    names = []
    for i in range(num_coef):
        names.append(r'a_{}'.format(i))
    for i in range(num_of_datasets):
        # непосредственно создание pandas таблицы
        param = np.concatenate((np.array(a[i]),np.array(sigma_a[i]), np.array(rel_sigma_a[i]))).reshape(3,num_coef).T
        output = pd.DataFrame(param, columns = ['coeffs_values', 'standard error', 'relative se, %'])
        output.insert(0, value = names, column = 'coeffs')

        # сохраним в таблицу csv
        if save_as_csv == True:
            output.to_csv('output_{}.csv'.format(i), index = False)

        # выведем таблицу
        print('Coeffs table {}: \n'.format(i))
        print(output)

        # выведем погрешность по оси Oy
        print('\nStandart_error_Y_{} = {:.3E}'.format(i,S_e[i]))

        # проебразование таблицы коэффициентов в латех код
        if to_latex == True:
            latex_output = output.to_latex(index = False, position = 'H', caption = 'Коэффициенты аппроксимации', label = 'coeffs_table')
            print('\n\nLatex code of coeffs table {}: \n'.format(i))
            print(latex_output)
            with open('coeffs_table_{}.tex'.format(i), 'w') as tf:
                tf.write(latex_output)

    # покажем график
    plt.show()

    pass

        