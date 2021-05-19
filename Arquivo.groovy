	#! groovy

	pipeline {
		agent{
		node {label 'IST5-flth229' }
	}
	
    //environment{
	
	//}

	stages 
		stage ('This is Stage 1')
			steps {
				echo "Hello World "
	}
	}
	stages 
		stage ('This is Stage 2')
			steps {
				echo "Hello World2 "}}
	stages 
		stage ('This is Stage 13')
			steps {
				echo "Hello World "
                }
            }
        }
    }