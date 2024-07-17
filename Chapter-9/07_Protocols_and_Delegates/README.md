# Protocols and Delegates

Protocols are a way to define a blueprint of methods, properties, and other requirements for a task or piece of functionality.

## Defining a Protocol

```swift
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
```

## Delegation

```swift
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
```
