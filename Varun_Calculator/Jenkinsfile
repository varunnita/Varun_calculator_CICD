// Jenkinsfile
// Declarative pipeline for the Python Calculator project.
// This file tells Jenkins exactly what to do when a build is triggered.

pipeline {

    // 'agent any' means: run this pipeline on any available Jenkins node (machine).
    agent any

    stages {

        // STAGE 1: Checkout - Get the latest code from GitHub
        stage('Checkout') {
            steps {
                // This pulls the latest code from the GitHub repository.
                // Jenkins does this automatically when using "Pipeline script from SCM",
                // but we include it here explicitly for clarity.
                checkout scm
            }
        }

        // STAGE 2: Install Dependencies
        // Our calculator uses only Python's built-in modules, so there's
        // nothing extra to install. In a real project, you'd install packages
        // from a requirements.txt file here.
        stage('Install Dependencies') {
            steps {
                echo 'No external dependencies to install.'
                echo 'This project uses only Python built-in modules.'
                // In a real project, you would run:
                // bat 'pip install -r requirements.txt'
            }
        }

        // STAGE 3: Run Tests - Automatically test the calculator
        stage('Run Tests') {
            steps {
                // Run the unittest test file.
                // 'bat' runs a Windows command. Use 'sh' instead on macOS/Linux.
                bat 'python -m unittest test_calculator.py -v'
            }
        }

        // STAGE 4: Build - Package the application
        stage('Build') {
            steps {
                echo 'Building the application...'
                // In a real Python project, you might create a distributable package.
                // For this project, we simulate packaging by echoing a message.
                echo 'Calculator application built successfully!'
            }
        }

        // STAGE 5: Deploy - Deliver the application
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Simulate deployment: run the calculator with a sample input
                // to prove the application works end to end.
                bat 'echo 1 & echo 5 & echo 3 | python calculator.py'
                echo '-------------------------------------------'
                echo 'Deployment simulation complete!'
                echo 'In a real environment, this stage would:'
                echo '  - Copy the app to a production server'
                echo '  - Restart the application service'
                echo '  - Notify the team via Slack or email'
                echo '-------------------------------------------'
            }
        }
    }

    // POST section: runs after all stages complete
    post {
        success {
            echo '=========================================='
            echo 'SUCCESS: All stages passed!'
            echo 'The Calculator app is tested and deployed.'
            echo '=========================================='
        }
        failure {
            echo '=========================================='
            echo 'FAILURE: Something went wrong!'
            echo 'Check the console output above for errors.'
            echo '=========================================='
        }
    }
}
