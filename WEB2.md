### **Before CSS**
Used \<font\> tag (e.g., \<font color="red">) <br>
font tag는 웹 페이지의 정보 자체와는 무관하다. <br>
정보가 아닌 것을 정보와 함께 담아두는 셈 <br>

```html
<!doctype html>
<html>
<head>
  <title>WEB - CSS</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html"><font color="red">WEB</font></a></h1>
  <ol>
    <li><a href="1.html"><font color="red">HTML</font></a></li>
    <li><a href="2.html"><font color="red">CSS</font></a></li>
    <li><a href="3.html"><font color="red">JavaScript</font></a></li>
  </ol>
  <h2>CSS</h2>
  <p>
    Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language.[1] Although most often used to set the visual style of web pages and user interfaces written in HTML and XHTML, the language can be applied to any XML document, including plain XML, SVG and XUL, and is applicable to rendering in speech, or on other media. Along with HTML and JavaScript, CSS is a cornerstone technology used by most websites to create visually engaging webpages, user interfaces for web applications, and user interfaces for many mobile applications.
  </p>
  </body>
  </html>
```


### **After CSS**
웹 브라우저가 처음 나왔을 때, HTML이 유일한 웹 언어였다. <br>
따라서 HTML을 통해 이 언어가 CSS라는 것을 명시해야 한다. <br>
a 태그의 색을 빨간색으로 바꾸는 style 태그는 다음과 같다.

```html
<style>
    a{
        color:red;  
    }
</style>
```
이와 같이, 디자인을 태그별로 설정함으로써 html에서 병렬로 코드를 적는 것에 비해 코드의 중복을 확실하게 줄일 수 있다.
- 코드 중복 방지
- 코드의 순수 정보성 보장


### **Basic CSS**
css는 html과 완전히 다른 언어이기 때문에 어떤 형태로든 css를 구분해서 표시해야 한다.
- \<style> 태그로 표시 : 동시 적용에 용이하나 각 항목에 적용하기 어려움
- style="color:red" : 동시 적용은 어렵지만 각 항목에 별도로 적용할 수 있음. 이런 방식을 style=""을 사용하는 것을 속성이라고 한다. 이는 css가 아니고 css 코드가 입력된다는 것을 암시하는 html의 속성이다. 

selector - 어느 태그에게 효과를 줄 것인지를 나타낸다
declaration - 태그에게 줄 효과. 여러 효과가 있는 경우 세미콜론(;)으로 구분한다.

### **Properties**
