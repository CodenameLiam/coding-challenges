// from https://www.linkedin.com/learning/code-challenges-javascript/available-books?u=57080313

class Book {
    constructor(title, author, ISBN, numCopies) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
        this.numCopies = numCopies;
    }

    getAvailability = () => {
        return this.numCopies <= 0 ? "out of stock" : this.numCopies <= 10 ? "low stock" : "in stock";
    };

    sell = (numSold) => {
        numSold = numSold ? numSold : 1;

        if (this.numCopies - numSold >= 0) {
            this.numCopies -= numSold;
        } else {
            console.error("Not enough copies in stock");
        }
    };

    restock = (numCopies) => {
        numCopies = numCopies ? numCopies : 5;
        this.numCopies += numCopies;
    };
}

let book1 = new Book("Title1", "Author1", "ISBN1", 12);

book1.restock(13);

console.log(book1);
