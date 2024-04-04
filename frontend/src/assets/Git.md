# javascript学习笔记







## base

javascript是一门解释性的编程语言,它一般用于配合html,css动态更新网页的内容.它一般在用户端运行,当然它也可以在服务器端运行.

我们可以使用**Application Programming Interfaces** (**APIs**) 来利用js实现很多有意思的功能.API分为`browsers APIs`和`third party APIs`,前者为浏览器自带的API,后者会第三方提供的API.

一般每一个标签页都会运行在一个单独的环境,于是js无法得到其他页的数据.这用于保证数据安全.

类似css,在html中js有如下方式引入:



**向页面中添加javascrip**

内部javascrip:向html文件`<head>`中加入`<script>`元素

```html
<script>
document.addEventListener("DOMContentLoaded", function() {
  function createParagraph() {
    let para = document.createElement('p');
    para.textContent = '你点击了这个按钮！';
    document.body.appendChild(para);
  }

  const buttons = document.querySelectorAll('button');

  for(let i = 0; i < buttons.length ; i++) {
    buttons[i].addEventListener('click', createParagraph);
  }
});

</script>
```

外部javascrip:将内部样式的`<scrip>`改为如下样式

```html
<script src="script.js" async></script>
```

内联javascript:

```html
<script>
    function createParagraph() {
      let para = document.createElement('p');
      para.textContent = 'You clicked the button!';
      document.body.appendChild(para);
    }
</script>
<button onclick="createParagraph()">Click me!</button>
```

> 同样的，内联样式不推荐使用，会污染html且低效

**脚本加载顺序**

javascrip一般调用于html文档头部，解析在html文档之前，这样存在隐患，需要加入事件监听器在html文档加载解析完毕后调用. . . 处js代码

```js
document.addEventListener("DOMContentLoaded", function() {
  . . .
});
```

对于外部示例，html使用了一种“异步“属性`async`和`defer`来解决

`async`使得浏览器在遇到`script`元素时不要中断后续html内容的加载,

```html
<script src="script.js" async></script>
```

上述情况下，脚本和 HTML 将一并加载，代码将顺利运行。但遇到多个外部javascript脚本时加载顺序无法确定。

使用`defer`脚本将按照在页面中出现的顺序加载和运行

```html
<script defer src="js/vendor/jquery.js"></script>

<script defer src="js/script2.js"></script>

<script defer src="js/script3.js"></script>
```

> async和defer无法用于内部加载方式



## 基本元素



### 变量(Variables)

**赋值和声明**

使用`var`或`let`来声明变量,初始化(赋值)

```javascript
let name;
name='Chros';
//或者
let name='Chros';
```



`var`和`let`声明方式的区别

- `var`允许初始化之后再声明,而`let`会报错

```javascript
myName = 'Chris';

function logName() {
  console.log(myName);
}

logName();

var myName;
```

- `var`允许多次声明相同变量，`let`不能

```javascript
var myName = 'Chris';
var myName = 'Bob';

//right use for let

let myName = 'Chris';
myName = 'Bob';
```

es8后推荐使用let

**变量命名规范**

字母开头，后接字母数字下划线

下划线开头在javaScript中有特殊含义



**变量类型**

- 数字(整型或浮点)

- 字符串(单引号或双引号)
- 布尔类型(true/false)
- 数组类型

```javascript
let myNameArray = ['Chris', 'Bob', 'Jim'];
let myNumberArray = [10,15,40];
myNameArray[0]; // should return 'Chris'
myNumberArray[2]; // should return 40
```

- 对象

```javascript
let dog = { name : 'Spot', breed : 'Dalmatian' };
dog.name='kerl'
```



### 运算符

javascript支持的运算符

| 运算符 | 名称                  | 作用                                                         | 示例                                                |
| :----- | :-------------------- | :----------------------------------------------------------- | :-------------------------------------------------- |
| `+`    | 加法                  | 两个数相加。                                                 | `6 + 9`                                             |
| `-`    | 减法                  | 从左边减去右边的数。                                         | `20 - 15`                                           |
| `*`    | 乘法                  | 两个数相乘。                                                 | `3 * 7`                                             |
| `/`    | 除法                  | 用右边的数除左边的数                                         | `10 / 5`                                            |
| `%`    | 求余 (有时候也叫取模) | 在你将左边的数分成同右边数字相同的若干整数部分后，返回剩下的余数 | `8 % 3` (返回 2，8 除以 3 的倍数，余下 2。)         |
| `**`   | 幂                    | 取底数的指数次方，即指数所指定的底数相乘。它在 EcmaScript 2016 中首次引入。 | `5 ** 5` (返回 3125，相当于 `5 * 5 * 5 * 5 * 5` 。) |
| `++`   | 自增                  |                                                              |                                                     |
| `--`   | 自减                  |                                                              |                                                     |

| 运算符 | 名称     | 作用                                           | 示例              | 等价于               |
| :----- | :------- | :--------------------------------------------- | :---------------- | :------------------- |
| `+=`   | 加法赋值 | 右边的数值加上左边的变量，然后再返回新的变量。 | `x = 3; x += 4;`  | `x = 3; x = x + 4;`  |
| `-=`   | 减法赋值 | 左边的变量减去右边的数值，然后再返回新的变量。 | `x = 6; x -= 3;`  | `x = 6; x = x - 3;`  |
| `*=`   | 乘法赋值 | 左边的变量乘以右边的数值，然后再返回新的变量。 | `x = 2; x *= 3;`  | `x = 2; x = x * 3;`  |
| `/=`   | 除法赋值 | 左边的变量除以右边的数值，然后再返回新的变量。 | `x = 10; x /= 5;` | `x = 10; x = x / 5;` |

| 运算符 | 名称       | 作用                           | 示例          |
| :----- | :--------- | :----------------------------- | :------------ |
| `===`  | 严格等于   | 测试左右值是否相同             | `5 === 2 + 4` |
| `!==`  | 严格不等于 | 测试左右值是否**不**相同       | `5 !== 2 + 3` |
| `<`    | 小于       | 测试左值是否小于右值。         | `10 < 6`      |
| `>`    | 大于       | 测试左值是否大于右值           | `10 > 20`     |
| <=     | 小于或等于 | 测试左值是否小于或等于右值。   | `3 <= 2`      |
| >=     | 大于或等于 | 测试左值是否大于或等于正确值。 | `5 >= 4`      |



>**备注：** 您可能会看到有些人在他们的代码中使用`==`和`!=`来判断相等和不相等，这些都是 JavaScript 中的有效运算符，但它们与`===`/`!==`不同，前者测试值是否相同，但是数据类型可能不同，而后者的严格版本测试值和数据类型是否相同。严格的版本往往导致更少的错误，所以我们建议您使用这些严格的版本。





### 字符串

在字符串中包含引号

```javascript
let sglDbl = 'Would you eat a "fish supper"?';
let dblSgl = "I'm feeling blue.";
sglDbl;
dblSgl;
```

转义字符使用反斜杠`\`

```javascript
let bigmouth = 'I\'ve got no right to take my place...';
bigmouth;
```

字符串连接使用`+`

```javascript
let response = one + 'I am fine — ' + two;
response;
```

或使用${}来包含变量

```js
newImage.setAttribute('src', `images/${image}`)
```



**数字转字符串**

1、直接用字符串和数字连接，数字会自动进行类型转换

```javascript
'Font'+233
```

2、每个数字都有一个`toString`的方法

```javascript
let myNum = 123;
let myString = myNum.toString();
typeof myString;
```



**字符串转数字**

`Number`对象把所有传给他的东西转换为一个数字

```javascript
let myString = '123';
let myNum = Number(myString);
typeof myNum;
```



#### 常用的字符串方法

`length`属性获取字符串长度

```javascript
let browserType = 'mozilla';
browserType.length;
```



`indexOf()`在较大字符串中查找字符串

```javascript
browserType.indexOf('zilla');
```



`slice(s,[e])`字符串提取切片[s,e),若没有包含第二个参数，则返回s之后的所有剩余字符

```javascript
browserType.slice(0,3);
```



`toLowerCase()`,`toUpperCase()`转换大小写



`replace`替换字符串中的字符，但要注意该函数不会修改原字符串，它只会返回修改后的副本。

```javascript
browserType=browserType.replace('moz','van');
```



`split(c)`函数会以字符c拆分字符串为**数组**



### 数组

javascript数组可以存储任何类型的元素

```js
let sequence = [1, 1, 2, 3, 5, 8, 13];
let random = ['tree', 795, [0, 1, 2]];
```

获取数组长度`length`属性

#### 常用的数组方法

`join(c)`方法将字符串数组中的每一项，使用字符c连接起来成为一个**字符串**

`toString()`方法将字符数组转化为**字符串**，但它不能指定连接符



使用`.push()`添加数组项，调用完成时返回新的数组长度

```js
var newLength = myArray.push('Bristol');
myArray;
newLength;
```

使用`.pop()`删除数组最后项，调用完成时返回已删除的项目

```js
let removedItem = myArray.pop();
myArray;
removedItem;

```



[`unshift()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) 和 [`shift()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/shift) 从功能上与 [`push()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/push) 和 [`pop()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/pop) 完全相同，只是它们分别作用于数组的开始，而不是结尾。



## JavaScript 代码块

### 循环

**for代码示例**

```js
var cats = ['Bill', 'Jeff', 'Pete', 'Biggles', 'Jasmin'];
var info = 'My cats are called ';
var para = document.querySelector('p');

for (var i = 0; i < cats.length; i++) {
  info += cats[i] + ', ';
}

para.textContent = info;
```

**遍历数组的便捷方式**

```js
const images = ['pic1.jpg', `pic2.jpg`, `pic3.jpg`, `pic4.jpg`, `pic5.jpg`];
for (const image of images) {
  const newImage = document.createElement('img');
  newImage.setAttribute('src', `images/${image}`);
  newImage.setAttribute('alt', alts[image]);
  thumbBar.appendChild(newImage);
  newImage.addEventListener('click', e => {
    displayedImage.src = e.target.src;
    displayedImage.alt = e.target.alt;
  });
}
```



### 匿名函数

创建一个没有名称的函数`founction(){};`

通常将匿名函数与事件处理程序一起使用，例如，如果单击相关按钮，以下操作将在函数内运行代码：

```js
var myButton = document.querySelector('button');

myButton.onclick = function() {
  alert('hello');
}
```



### 事件

#### 使用addEventListener添加事件处理器

激发事件的对象有一个 `addEventListener (type, listener)`方法，这是添加事件处理程序的推荐机制，当该对象触发指定的事件时，指定的回调函数就会被执行。

addEventListener(type, listener)接收两个参数：

- type:表示监听[事件类型](https://developer.mozilla.org/zh-CN/docs/Web/Events)的大小写敏感的字符串。
- listener:当所监听的事件类型触发时，会接收到一个事件通知（实现了 [`Event`](https://developer.mozilla.org/zh-CN/docs/Web/API/Event) 接口的对象）对象。`listener` 必须是一个实现了 [`EventListener`](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener) 接口的对象，或者是一个[函数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Functions)。有关回调本身的详细信息，请参阅[事件监听回调](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener#事件监听回调)

```js
const btn = document.querySelector("button");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}

function changeBackground() {
  const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
  document.body.style.backgroundColor = rndCol;
}

btn.addEventListener("click", changeBackground);
```



#### 移除事件处理器

- 使用`removeEventListener("click", changeBackground);`移除事件监听器

- 事件处理程序也可以删除，方法是向 `addEventListener ()`传递一个 `AbortSignal`(作为第三个参数)，然后在拥有 `AbortSignal `的控制器上调用 `abort ()`。例如，要添加一个事件处理程序，我们可以使用一个 `AbortSignal` 删除该事件处理程序:

```js
//添加事件监听器
const controller = new AbortController();

btn.addEventListener(
  "click",
  () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    document.body.style.backgroundColor = rndCol;
  },
  { signal: controller.signal }
); // pass an AbortSignal to this handler

//移除事件监听器
controller.abort(); // removes any/all event handlers associated with this controller

```



#### 事件处理器属性

可以激发事件的对象(如buttons)通常也具有名称为 on 的事件名的属性。例如，元素具有 onclick 属性。这称为事件处理程序属性。若要侦听事件，可以将处理程序函数分配给属性。

```javascript
const btn = document.querySelector("button");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}

btn.onclick = () => {
  const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
  document.body.style.backgroundColor = rndCol;
};

//或者赋值为函数名
function bgChange() {
  const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
  document.body.style.backgroundColor = rndCol;
}

btn.onclick = bgChange;
```



> 注意：使用addEventListener可以多次添加事件处理器
>
> ```js
> element.addEventListener("click", function1);
> element.addEventListener("click", function2);
> ```
>
> 而使用事件处理器属性却只能关联一个事件处理函数
>
> ```js
> element.onclick = function1;
> element.onclick = function2;
> //以上function2会覆盖function1
> ```

#### 事件对象

**事件对象**，它被自动传递给事件处理函数，以提供额外的功能和信息

```js
function bgChange(e) {
  const rndCol = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')';
  e.target.style.backgroundColor = rndCol;
  console.log(e);
}

btn.addEventListener('click', bgChange);
```

> `e.target` ——它指的是按钮本身。事件对象 `e` 的 `target` 属性始终是事件刚刚发生的元素的引用。

#### 事件的冒泡及捕获

当一个事件发生在具有父元素的元素上时，现代浏览器运行两个不同的阶段 - 捕获阶段和冒泡阶段。在捕获阶段：

- 浏览器检查元素的最外层祖先`<html>`，是否在捕获阶段中注册了一个`onclick`事件处理程序，如果是，则运行它。
- 然后，它移动到`<html>`中单击元素的下一个祖先元素，并执行相同的操作，然后是单击元素再下一个祖先元素，依此类推，直到到达实际点击的元素。

在冒泡阶段，恰恰相反：

- 浏览器检查实际点击的元素是否在冒泡阶段中注册了一个`onclick`事件处理程序，如果是，则运行它
- 然后它移动到下一个直接的祖先元素，并做同样的事情，然后是下一个，等等，直到它到达`<html>`元素。

在现代浏览器中，默认情况下，所有事件处理程序都在**冒泡阶段**进行注册。

**使用stopPropagation()阻断冒泡链**

标准事件对象具有可用的名为 [`stopPropagation()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/stopPropagation)的函数，当在事件对象上调用该函数时，它只会让当前事件处理程序运行，但事件不会在**冒泡**链上进一步扩大，因此将不会有更多事件处理器被运行 (不会向上冒泡)。

```javascript
video.onclick = function(e) {
  e.stopPropagation();
  video.play();
};
```



## javaScript对象



## 客户端 Web API

### DOM

#### 基本dom操作

**元素选择**

[`Document.querySelector()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelector)允许你使用 CSS 选择器选择元素，使用很方便。上面的`querySelector()`调用会匹配它在文档中遇到的第一个[`<a>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a)元素。如果想对多个元素进行匹配和操作，你可以使用[`Document.querySelectorAll()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelectorAll)，这个方法匹配文档中每个匹配选择器的元素，并把它们的引用存储在一个[array](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/First_steps/Arrays)中。

**创建和添加元素**

例如：用[`Document.createElement()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createElement)创建一个新的段落，用与之前相同的方法赋予相同的文本

```js
var para = document.createElement('p');
para.textContent = 'We hope you enjoyed the ride.';
```

可以用[`Node.appendChild()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/appendChild)方法在后面追加新的段落

```js
sect.appendChild(para);
```

> 注意，文本text也是一个节点，可用以上方式追加到<p>中
>
> ```js
> var text = document.createTextNode(' — the premier source for web development knowledge.');
> var linkPara = document.querySelector('p');
> linkPara.appendChild(text);
> ```

**移动和删除元素**

如果你想把具有内部链接的段落移到 sectioin 的底部，简单的做法是：

```
sect.appendChild(linkPara);
```

这样可以把段落下移到 section 的底部。你可能想过要做第二个副本，但是情况并非如此 — `linkPara`是指向该段落唯一副本的引用。如果你想做一个副本并也把它添加进去，只能用[`Node.cloneNode()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/cloneNode) 方法来替代。

删除节点也非常的简单，至少，你拥有要删除的节点和其父节点的引用。在当前情况下，我们只要使用[`Node.removeChild()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/removeChild)即可，如下：

```js
sect.removeChild(linkPara);
```

要删除一个仅基于自身引用的节点可能稍微有点复杂，这也是很常见的。没有方法会告诉节点删除自己，所以你必须像下面这样操作。

```js
linkPara.parentNode.removeChild(linkPara);
```

把上述代码行加到你的代码中去

**样式操作**

通过 JavaScript 以不同的方式来操作 CSS 样式是可能的。

首先，使用 [`Document.stylesheets`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/styleSheets)返回[`CSSStyleSheet`](https://developer.mozilla.org/zh-CN/docs/Web/API/CSSStyleSheet)数组，获取绑定到文档的所有样式表的序列。然后添加/删除想要的样式。然而，我们并不想扩展这些特性，因此它们在操作样式方面有点陈旧和困难，而现在有了更容易的方法。

第一种方法是直接在想要动态设置样式的元素内部添加内联样式。这是用[`HTMLElement.style` (en-US)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)属性来实现。这个属性包含了文档中每个元素的内联样式信息。你可以设置这个对象的属性直接修改元素样式。

1. 要做个例子，把下面的代码行加到我们的例子中：

   ```js
   para.style.color = 'white';
   para.style.backgroundColor = 'black';
   para.style.padding = '10px';
   para.style.width = '250px';
   para.style.textAlign = 'center';
   ```

2. 重新载入页面，你将看到样式已经应用到段落中。如果在浏览器的

   Page Inspector/DOM inspector

   中查看段落，你会看到这些代码的确为文档添加了内联样式：

   ```js
   <p style="color: white; background-color: black; padding: 10px; width: 250px; text-align: center;">We hope you enjoyed the ride.</p>
   ```

> **备注：** CSS 样式的 JavaSript 属性版本以小驼峰式命名法书写，而 CSS 版本带连接符号（`backgroundColor` 对 `background-color`）。确保你不会混淆，否则就不能工作。

现在我们来看看另一个操作文档样式的常用方法。

1. 删除之前添加到 JavaScript 中的五行代码。

2. 在 HTML 的`<head>`中添加下列代码 :

   ```html
   <style>
   .highlight {
     color: white;
     background-color: black;
     padding: 10px;
     width: 250px;
     text-align: center;
   }
   </style>
   ```

3. 现在我们改为使用 HTML 操作的常用方法 `Element.setAttribute()`— 这里有两个参数，你想在元素上设置的属性，你要为它设置的值。在这种情况下，我们在段落中设置类名为 highlight：

   ```js
   para.setAttribute('class', 'highlight');
   ```

4. 刷新页面，看不到改变 — CSS 仍然应用到段落，但是这次给出 CSS 规则选择的类不是内联 CSS 样式。

两种方式各有优缺点，选择哪种取决于你自己。第一种方式无需安装，适合简单应用，第二种方式更加正统（没有 CSS 和 JavaScript 的混合，没有内联样式，而这些被认为是不好的体验）。当你开始构建更大更具吸引力的应用时，你可能会更多地使用第二种方法，但这完全取决于你自己。



#### 从服务器获取数据

 [Fetch API](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API)。它允许页面中运行的 JavaScript 向服务器发起 [HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP) 请求来获取特定的资源。当服务器提供了这些资源时，JavaScript 可以使用这些数据更新页面（通常是通过使用 [DOM 操作 API](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)）。请求的数据通常是 [JSON](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Objects/JSON)，这是一种很好的传输结构化的格式，但也可以是 HTML 或纯文本。



使用示例：

```html
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Fetch starting point</title>

    <style>
      html, pre {
        font-family: sans-serif;
      }

      body {
        width: 500px;
        margin: 0 auto;
        background-color: #ccc;
      }

      pre {
        line-height: 1.5;
        letter-spacing: 0.05rem;
        padding: 1rem;
        background-color: white;
      }

      label {
        width: 200px;
        margin-right: 33px;
      }

      select {
        width: 350px;
        padding: 5px;
      }

    </style>

  </head>

  <body>
    <h1>Fetch starting point</h1>

    <form>
      <label for="verse-choose">Choose a verse</label>
      <select id="verse-choose" name="verse-choose">
        <option>Verse 1</option>
        <option>Verse 2</option>
        <option>Verse 3</option>
        <option>Verse 4</option>
      </select>
    </form>

    <h2>The Conqueror Worm, <em>Edgar Allen Poe, 1843</em></h2>

    <pre>

    </pre>

    <script>

    </script>
  </body>
</html>
```

添加的javascript代码：

```js
const verseChoose = document.querySelector('select');
const poemDisplay = document.querySelector('pre');

verseChoose.addEventListener('change', () => {
  const verse = verseChoose.value;
  updateDisplay(verse);
});
function updateDisplay(verse) {

}
verse = verse.replace(' ', '').toLowerCase();
const url = `${verse}.txt`;

// 调用 `fetch()`，传入 URL。
fetch(url)
  // fetch() 返回一个 promise。当我们从服务器收到响应时，
  // 会使用该响应调用 promise 的 `then()` 处理器。
  .then((response) => {
    // 如果请求没有成功，我们的处理器会抛出错误。
    if (!response.ok) {
      throw new Error(`HTTP 错误：${response.status}`);
    }
    // 否则（如果请求成功），我们的处理器通过调用
    // response.text() 以获取文本形式的响应，
    // 并立即返回 `response.text()` 返回的 promise。
    return response.text();
  })
  // 若成功调用 response.text()，会使用返回的文本来调用 `then()` 处理器，
  // 然后我们将其拷贝到 `poemDisplay` 框中。
  .then((text) => poemDisplay.textContent = text)
  // 捕获可能出现的任何错误，
  // 并在 `poemDisplay` 框中显示一条消息。
  .catch((error) => poemDisplay.textContent = `获取诗歌失败：${error}`);

```

