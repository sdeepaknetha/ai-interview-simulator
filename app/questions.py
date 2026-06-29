questions_data = {
    "python": {
        "easy": [
            {"question": "What is Python?"},
            {"question": "What is a list in Python?"},
            {"question": "What is the difference between a list and a tuple?"},
            {"question": "What is a dictionary in Python?"},
            {"question": "What is an if-else statement?"},
            {"question": "What is a for loop in Python?"},
            {"question": "What is a function in Python?"},
            {"question": "What is the use of the print() function?"},
            {"question": "What is a string in Python?"},
            {"question": "What is the difference between int and float?"}
        ],
        "medium": [
            {"question": "Explain OOP in Python."},
            {"question": "What are decorators in Python?"},
            {"question": "What is the difference between deep copy and shallow copy?"},
            {"question": "Explain list comprehension with an example."},
            {"question": "What are lambda functions?"},
            {"question": "What is exception handling in Python?"},
            {"question": "What is the difference between append() and extend()?"},
            {"question": "What are Python generators?"},
            {"question": "Explain the concept of inheritance in Python."},
            {"question": "What is the difference between @staticmethod and @classmethod?"}
        ],
        "hard": [
            {"question": "Explain multithreading in Python."},
            {"question": "What is GIL in Python?"},
            {"question": "Explain metaclasses in Python."},
            {"question": "What is asyncio and how does it work?"},
            {"question": "Explain memory management in Python."},
            {"question": "What are context managers and how do you create one?"},
            {"question": "Explain the difference between multiprocessing and multithreading."},
            {"question": "What is monkey patching in Python?"},
            {"question": "Explain Python descriptors."},
            {"question": "What are coroutines in Python?"}
        ]
    },
    "java": {
        "easy": [
            {"question": "What is Java?"},
            {"question": "What is JDK, JRE, and JVM?"},
            {"question": "What is the difference between == and .equals()?"},
            {"question": "What is a class in Java?"},
            {"question": "What is an object in Java?"},
            {"question": "What are primitive data types in Java?"},
            {"question": "What is a constructor in Java?"},
            {"question": "What is the use of the main() method?"},
            {"question": "What is a String in Java?"},
            {"question": "What is an array in Java?"}
        ],
        "medium": [
            {"question": "Explain OOP concepts in Java."},
            {"question": "What is multithreading in Java?"},
            {"question": "What is the difference between ArrayList and LinkedList?"},
            {"question": "Explain exception handling in Java."},
            {"question": "What is the difference between interface and abstract class?"},
            {"question": "What is Java Collections Framework?"},
            {"question": "Explain the concept of polymorphism in Java."},
            {"question": "What is the difference between final, finally, and finalize?"},
            {"question": "What are generics in Java?"},
            {"question": "What is the difference between HashMap and Hashtable?"}
        ],
        "hard": [
            {"question": "Explain JVM internals."},
            {"question": "What is garbage collection in Java?"},
            {"question": "Explain Java memory model."},
            {"question": "What are design patterns? Explain Singleton pattern."},
            {"question": "What is the difference between synchronized and volatile?"},
            {"question": "Explain Java Stream API."},
            {"question": "What are lambda expressions in Java 8?"},
            {"question": "Explain Spring Boot architecture."},
            {"question": "What is dependency injection?"},
            {"question": "Explain microservices with Java."}
        ]
    },
    "frontend": {
        "easy": [
            {"question": "What is HTML?"},
            {"question": "What is CSS?"},
            {"question": "What is the difference between div and span?"},
            {"question": "What is a CSS selector?"},
            {"question": "What is the box model in CSS?"},
            {"question": "What is the difference between inline and block elements?"},
            {"question": "What is JavaScript?"},
            {"question": "What is the DOM?"},
            {"question": "What is a media query in CSS?"},
            {"question": "What is the difference between id and class in HTML?"}
        ],
        "medium": [
            {"question": "Explain Flexbox in CSS."},
            {"question": "What is CSS Grid?"},
            {"question": "Explain event bubbling in JavaScript."},
            {"question": "What is the difference between let, const, and var?"},
            {"question": "What is a promise in JavaScript?"},
            {"question": "Explain async/await in JavaScript."},
            {"question": "What is React and why is it used?"},
            {"question": "What are React hooks?"},
            {"question": "What is the virtual DOM?"},
            {"question": "Explain REST API consumption in frontend."}
        ],
        "hard": [
            {"question": "Explain event delegation in JavaScript."},
            {"question": "What is React virtual DOM and how does reconciliation work?"},
            {"question": "Explain webpack and bundling."},
            {"question": "What is server-side rendering vs client-side rendering?"},
            {"question": "Explain React context API."},
            {"question": "What is Redux and when should you use it?"},
            {"question": "Explain lazy loading in React."},
            {"question": "What are web workers?"},
            {"question": "Explain CORS and how to handle it."},
            {"question": "What is progressive web app (PWA)?"}
        ]
    },
    "backend": {
        "easy": [
            {"question": "What is backend development?"},
            {"question": "What is a server?"},
            {"question": "What is an API?"},
            {"question": "What is HTTP?"},
            {"question": "What is a database?"},
            {"question": "What is the difference between GET and POST requests?"},
            {"question": "What is JSON?"},
            {"question": "What is authentication?"},
            {"question": "What is a REST API?"},
            {"question": "What is a web framework?"}
        ],
        "medium": [
            {"question": "What is REST API and its principles?"},
            {"question": "Explain MVC architecture."},
            {"question": "What is middleware in backend development?"},
            {"question": "What is the difference between SQL and NoSQL?"},
            {"question": "Explain JWT authentication."},
            {"question": "What is session management?"},
            {"question": "What is caching and why is it used?"},
            {"question": "Explain database indexing."},
            {"question": "What is rate limiting?"},
            {"question": "Explain CORS in backend development."}
        ],
        "hard": [
            {"question": "Explain microservices architecture."},
            {"question": "What is message queuing? Explain RabbitMQ or Kafka."},
            {"question": "Explain database sharding."},
            {"question": "What is load balancing?"},
            {"question": "Explain CAP theorem."},
            {"question": "What is GraphQL and how is it different from REST?"},
            {"question": "Explain distributed systems."},
            {"question": "What is containerization with Docker?"},
            {"question": "Explain horizontal vs vertical scaling."},
            {"question": "What is event-driven architecture?"}
        ]
    },
    "fullstack": {
        "easy": [
            {"question": "What is full stack development?"},
            {"question": "What is the difference between frontend and backend?"},
            {"question": "What is a web application?"},
            {"question": "What is HTML used for?"},
            {"question": "What is a database?"},
            {"question": "What is version control?"},
            {"question": "What is Git?"},
            {"question": "What is deployment?"},
            {"question": "What is a framework?"},
            {"question": "What is an API?"}
        ],
        "medium": [
            {"question": "Explain frontend vs backend responsibilities."},
            {"question": "What is the MERN stack?"},
            {"question": "What is the difference between REST and GraphQL?"},
            {"question": "How do you connect frontend to backend?"},
            {"question": "What is state management?"},
            {"question": "Explain authentication in full stack apps."},
            {"question": "What is CRUD?"},
            {"question": "What is ORM?"},
            {"question": "Explain the request-response cycle."},
            {"question": "What is Docker and why is it useful?"}
        ],
        "hard": [
            {"question": "How do you design scalable applications?"},
            {"question": "Explain CI/CD pipeline for full stack apps."},
            {"question": "What is server-side rendering vs client-side rendering?"},
            {"question": "Explain database optimization techniques."},
            {"question": "How do you handle security in full stack apps?"},
            {"question": "What is microservices vs monolithic architecture?"},
            {"question": "Explain WebSockets and real-time communication."},
            {"question": "What is cloud deployment? Explain AWS or GCP basics."},
            {"question": "How do you optimize web application performance?"},
            {"question": "Explain system design for a social media app."}
        ]
    },
    "data_analyst": {
        "easy": [
            {"question": "What is SQL?"},
            {"question": "What is a database?"},
            {"question": "What is data analysis?"},
            {"question": "What is Excel used for in data analysis?"},
            {"question": "What is a primary key?"},
            {"question": "What is the difference between COUNT and SUM?"},
            {"question": "What is a foreign key?"},
            {"question": "What is data cleaning?"},
            {"question": "What is a pivot table?"},
            {"question": "What is the difference between mean, median, and mode?"}
        ],
        "medium": [
            {"question": "Explain SQL joins with examples."},
            {"question": "What is GROUP BY in SQL?"},
            {"question": "What is data visualization?"},
            {"question": "Explain the difference between HAVING and WHERE."},
            {"question": "What is a subquery in SQL?"},
            {"question": "What is Pandas in Python?"},
            {"question": "Explain data normalization."},
            {"question": "What is an ETL process?"},
            {"question": "What is the difference between OLAP and OLTP?"},
            {"question": "What is a data warehouse?"}
        ],
        "hard": [
            {"question": "Explain database indexing and query optimization."},
            {"question": "What is window function in SQL?"},
            {"question": "Explain A/B testing."},
            {"question": "What is statistical significance?"},
            {"question": "Explain correlation vs causation."},
            {"question": "What is time series analysis?"},
            {"question": "Explain data pipeline architecture."},
            {"question": "What is Spark and when is it used?"},
            {"question": "Explain cohort analysis."},
            {"question": "What is data governance?"}
        ]
    },
    "data_scientist": {
        "easy": [
            {"question": "What is data science?"},
            {"question": "What is machine learning?"},
            {"question": "What is the difference between supervised and unsupervised learning?"},
            {"question": "What is a dataset?"},
            {"question": "What is Python used for in data science?"},
            {"question": "What is data preprocessing?"},
            {"question": "What is a feature in machine learning?"},
            {"question": "What is a label in machine learning?"},
            {"question": "What is linear regression?"},
            {"question": "What is a confusion matrix?"}
        ],
        "medium": [
            {"question": "What is machine learning model evaluation?"},
            {"question": "Explain cross-validation."},
            {"question": "What is the difference between classification and regression?"},
            {"question": "What is feature engineering?"},
            {"question": "Explain decision trees."},
            {"question": "What is random forest?"},
            {"question": "What is gradient boosting?"},
            {"question": "Explain dimensionality reduction."},
            {"question": "What is PCA?"},
            {"question": "Explain the bias-variance tradeoff."}
        ],
        "hard": [
            {"question": "Explain overfitting and underfitting and how to handle them."},
            {"question": "What is deep learning and how is it different from ML?"},
            {"question": "Explain neural networks."},
            {"question": "What is NLP and its applications?"},
            {"question": "Explain transformer architecture."},
            {"question": "What is reinforcement learning?"},
            {"question": "Explain hyperparameter tuning."},
            {"question": "What is model deployment?"},
            {"question": "Explain ensemble methods."},
            {"question": "What is AutoML?"}
        ]
    },
    "devops": {
        "easy": [
            {"question": "What is DevOps?"},
            {"question": "What is version control?"},
            {"question": "What is Git?"},
            {"question": "What is a server?"},
            {"question": "What is Linux?"},
            {"question": "What is a shell script?"},
            {"question": "What is deployment?"},
            {"question": "What is monitoring in DevOps?"},
            {"question": "What is a virtual machine?"},
            {"question": "What is cloud computing?"}
        ],
        "medium": [
            {"question": "What is CI/CD?"},
            {"question": "What is Docker?"},
            {"question": "What is a container?"},
            {"question": "Explain Jenkins pipeline."},
            {"question": "What is infrastructure as code?"},
            {"question": "What is Ansible?"},
            {"question": "What is Terraform?"},
            {"question": "Explain blue-green deployment."},
            {"question": "What is load balancing?"},
            {"question": "What is a reverse proxy?"}
        ],
        "hard": [
            {"question": "Explain Docker and Kubernetes architecture."},
            {"question": "What is Kubernetes orchestration?"},
            {"question": "Explain service mesh architecture."},
            {"question": "What is GitOps?"},
            {"question": "Explain chaos engineering."},
            {"question": "What is observability in DevOps?"},
            {"question": "Explain zero downtime deployment strategies."},
            {"question": "What is container security?"},
            {"question": "Explain multi-cloud strategy."},
            {"question": "What is site reliability engineering (SRE)?"}
        ]
    },
    "cloud": {
        "easy": [
            {"question": "What is cloud computing?"},
            {"question": "What are the types of cloud services?"},
            {"question": "What is AWS?"},
            {"question": "What is the difference between public and private cloud?"},
            {"question": "What is a virtual machine in cloud?"},
            {"question": "What is cloud storage?"},
            {"question": "What is SaaS?"},
            {"question": "What is PaaS?"},
            {"question": "What is IaaS?"},
            {"question": "What is a cloud region?"}
        ],
        "medium": [
            {"question": "What are cloud service models?"},
            {"question": "Explain AWS EC2."},
            {"question": "What is S3 in AWS?"},
            {"question": "What is auto-scaling?"},
            {"question": "Explain cloud security basics."},
            {"question": "What is a VPC in AWS?"},
            {"question": "What is serverless computing?"},
            {"question": "Explain AWS Lambda."},
            {"question": "What is a CDN?"},
            {"question": "What is cloud cost optimization?"}
        ],
        "hard": [
            {"question": "Explain AWS architecture for a scalable web app."},
            {"question": "What is multi-region deployment?"},
            {"question": "Explain disaster recovery in cloud."},
            {"question": "What is cloud native architecture?"},
            {"question": "Explain Kubernetes on cloud."},
            {"question": "What is edge computing?"},
            {"question": "Explain cloud compliance and governance."},
            {"question": "What is a hybrid cloud strategy?"},
            {"question": "Explain cloud migration strategies."},
            {"question": "What is FinOps in cloud?"}
        ]
    },
    "hr": {
        "easy": [
            {"question": "Tell me about yourself."},
            {"question": "What are your strengths?"},
            {"question": "What are your weaknesses?"},
            {"question": "Why do you want this job?"},
            {"question": "Where do you see yourself in 5 years?"},
            {"question": "What is your greatest achievement?"},
            {"question": "Are you a team player?"},
            {"question": "What motivates you?"},
            {"question": "Do you work well under pressure?"},
            {"question": "What are your hobbies?"}
        ],
        "medium": [
            {"question": "Why should we hire you?"},
            {"question": "Describe a challenging situation and how you handled it."},
            {"question": "How do you handle conflicts at work?"},
            {"question": "What do you know about our company?"},
            {"question": "How do you prioritize your work?"},
            {"question": "Describe your ideal work environment."},
            {"question": "How do you handle feedback and criticism?"},
            {"question": "What is your leadership style?"},
            {"question": "How do you stay updated with industry trends?"},
            {"question": "What salary do you expect?"}
        ],
        "hard": [
            {"question": "Describe a failure and what you learned from it."},
            {"question": "Tell me about a time you disagreed with your manager."},
            {"question": "How would you handle an underperforming team member?"},
            {"question": "Describe a time you led a project under pressure."},
            {"question": "How do you handle ambiguity at work?"},
            {"question": "Tell me about a time you had to make a difficult decision."},
            {"question": "How do you build relationships with difficult colleagues?"},
            {"question": "Describe a time you went above and beyond."},
            {"question": "How do you handle multiple competing priorities?"},
            {"question": "Where do you see this industry in 10 years?"}
        ]
    }
}
