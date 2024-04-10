function sayHello(name) {
    name = name || 'World';
    console.log('Hello ' + name + '!');
}

sayHello('Wesley'); // Hello Wesley!
sayHello(); // Hello World!