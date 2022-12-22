# Алгоритм сиракузской последовательности
В данном репозитории представлена программа, вычисляющая сиракузскую последовательность
## Описание алгоритма
1) берём любое натуральное число N;
2) если оно чётное, то делим его на 2;
3) если оно нечётное, то умножаем на 3 и прибавляем 1 (получаем 3N + 1);
4) над полученным числом выполняем те же самые действия, и так далее.
![Визуализация работы алгоритма](https://github.com/vveessdv/VvPD_PR_5/blob/main/picture.jpg?raw=true)

Подробнее об алгоритме читайте [здесь](https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0_%D0%9A%D0%BE%D0%BB%D0%BB%D0%B0%D1%82%D1%86%D0%B0)

Сложность алгоритма $O(n)$.
## Примеры кода
```
>>> syracuse_sequence(11)
[11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Также в коде представлена функция, для нахождения максимального числа это последовательности
_Ассимптотика возможных реализаций:_
* [ ] $O(n)$
* [ ] $O(2n)$
* [x] $O(n+n*log{2}(n))$
