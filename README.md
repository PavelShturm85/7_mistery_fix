# Решатель квадратных уравнений

This function counting the quadratic equation.

# Как использовать

Three values are transferred to the function get_roots(a, b, c). Then the quadratic equation is considered.

   - If a=0 the function linear, not quadratic.
   - The square root can not extracted if discriminant less then 0.
   - If discriminant is 0, then roots of the quadratic equation 1.
   - If discriminant > 0, then roots of the quadratic equation 2.

```python
from math import sqrt

root1 = (-b - sqrt(discriminant)) / (2 * a)
root2 = (-b + sqrt(discriminant)) / (2 * a)
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
