# ML_DZ1
Что было сделано:
1. Был проведен EDA данных: начиная с анализа сырых данных и заканчивая их обработкой в используемый финально вид. Были обработаны дубликаты (удалены), пропуски (заполнены медианами), удалены трудно обрабатываемые столбцы (name и torque), очищены числовые столбцы от лишних строковых значений. Дополнительно был построен дашборд по датасету, который оказался особенно информативен при обработке данных, так как на основании него сразу можно было получить ответы на все вопросы о данных.
2. Визуализации: помимо требуемых в задании (визуализация распределения признаков и их корреляции с целевой переменной) были также построены дополнительные графики, отражающие поведение целевой переменной с категориальными переменными. Основные задачи по визуализации касались только вещественных показателей.
3. Построены несколько варианты линейных моделей:
    На вещественных данных: дефолтная линейная регрессия, со стандартизацией данных, с Лассо регуляризацией (обычная и с GridSearch, который показал alpha = 8901, веса почти не занулялись, так как были гораздо выше порога, а зануление доп весов сказывалось на худшем качестве) и Elastic Net (GridSearch дал модель с alpha = 100 и l1 = 0)
    На всех переменных (добавление категориальных переменных):


