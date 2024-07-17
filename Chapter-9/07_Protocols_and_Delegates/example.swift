// Example of Protocols and Delegates

protocol Greetable {
    func greet()
}

class Person: Greetable {
    var name: String

    init(name: String) {
        self.name = name
    }

    func greet() {
        print("Hello, my name is \(name).")
    }
}

let person = Person(name: "John")
person.greet()

// Delegation
protocol DataSource {
    func fetchData() -> String
}

class DataFetcher {
    var dataSource: DataSource?

    func getData() {
        if let data = dataSource?.fetchData() {
            print("Data: \(data)")
        } else {
            print("No data source.")
        }
    }
}

class APIDataSource: DataSource {
    func fetchData() -> String {
        return "Data from API"
    }
}

let dataFetcher = DataFetcher()
let apiDataSource = APIDataSource()
dataFetcher.dataSource = apiDataSource
dataFetcher.getData()
