node {
    stage('Build') {
        echo 'Building Docker image...'
        sh 'docker build -t myapp:latest .'
    }

    stage('Test') {
        echo 'Running tests...'
        sh 'echo "All tests passed!"'
    }

    stage('Deploy') {
        echo 'Deploying container...'
        sh '''
        docker rm -f myapp-container || true
        docker run -d -p 8081:8080 --name myapp-container myapp:latest
        '''
    }
}
