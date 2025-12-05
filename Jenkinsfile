pipeline {
    agent any

    environment {
        SELENOID_USER = credentials('selenoid-user')
        SELENOID_PASS = credentials('selenoid-pass')
        SELENOID_HOST = 'selenoid.autotests.cloud'
        BROWSER_VERSION = '128.0'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ВАШ_РЕПОЗИТОРИЙ.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=tests/allure-results'
            }
        }

        stage('Allure report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'tests/allure-results']]
            }
        }
    }
}
