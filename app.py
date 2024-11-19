from flask import Flask, render_template, request

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Список возрастов для выбора в форме
ages = ['18', '19', '20', '21', '22', '23', '24', '25']

@app.route('/')
def index():
    return render_template('index.html', ages=ages)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        # Сохраняем данные в словарь
        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }

        # Возвращаем страницу с данными пользователя
        return render_template('index.html', user_data=user_data, ages=ages)

if __name__ == '__main__':
    app.run(debug=True)