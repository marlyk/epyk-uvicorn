
![](https://raw.githubusercontent.com/marlyk/epyk-uvicorn/master/static/images/logo.ico)

### Epyk Uvicorn!


An easy way to use Epyk within a Uvicorn App

Uvicorn server is an excellent alternative to Node or Deno server. The design on top of Asyncio will improve a lot the server performances.
It is an excellent opportunity to stay full stack in Python !!! 

Uvicorn is a lightning-fast ASGI server, built on uvloop and httptools.

Until recently Python has lacked a minimal low-level server/application interface for asyncio frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all asyncio frameworks.

Requirements: Python 3.5, 3.6, 3.7, 3.8

Presentation
================================
This package will make a simple interface between the back and the front end generation.
For advanced use of Uvicon please refer to the [official website](https://www.uvicorn.org/)

This repository will deal with common and simple examples to demonstrate how to integrate Epyk to a Uvicorn environment.

Epyk can be used mainly in two different ways:

- Generating static or semi static (with Jinja) templates which will then be updated by Django
- Producing on the fly template within the views

This project will provide example on the different ways of using Epyk templates.

Quickstart
================================

Install uvicorn

> pip install uvicorn

Install Epyk

> pip install epyk

Please make sure the latest version of those libraries are installed


```py
async def test(scope, receive, send):
  page = Report()
  page.headers.dev()
  div = page.ui.div("Hellow World!")
  button = page.ui.button("Click Me")
  div.style.css.color = 'red'
  button.click([
    page.js.alert("Clicked")
  ])

  await send({
    'type': 'http.response.start',
    'status': 200,
    'headers': [
      [b'content-type', b'text/html'],
    ]
  })

  await send({
    'type': 'http.response.body',
    'body': page.outs.html().encode('utf-8'),
  })


if __name__ == "__main__":
    uvicorn.run("server:test", host="127.0.0.1", port=5000, log_level="info", reload=True)
```


Repo Architecture
================================

This repository is quite simple to show case the use of Epyk.

<div align="center" >
    <img src="https://github.com/marlyk/epyk-uvicorn/blob/master/static/images/details.PNG?raw=true">
</div>

In an full stack Python environment Epyk reports should be used within function and the page object should be
then retrieve to defined the output container.

Template.py will generate static HTML templates from the Epyk report objects whereas the server on his side will either
load the HTML static pages directly (to speed up the client response) or build this directly on the fly to return something
really bespoke to the HTTP query.

Indeed we can imagine in the second case that according to the users, the parameters passed in the URL the page will be
totally different.

Epyk make easy the management or dynamic templates on the UI side directly from Python.


Design Principle
================================

The design is similar to any moder web server the different here is that the code is generated from Python.
Epyk is designed to generate a rich HTML and JavaScript code which can be used by any browser.

The code will rely by default on external JavaScript packages which will be retrieved from CDNJS directly.

It is possible to install the packages locally from the npm command and to use this directly.

The standatd design is as below. Namely Epyk pages are used to generate HTML artefact which will then be used directly by the 
server the render the page.

It is possible also to generate the page on the fly, it the structure of the page is quite different.
This can easily adapt the page to the data without having to create multiple static reports.

<div align="center" >
    <img src="https://github.com/marlyk/epyk-uvicorn/blob/master/static/images/server_archi_1.PNG?raw=truee">
</div>

The concept is quite simple and it is based on components. Epyk is structure in simple components with some predefined styles and events.
Nearly all the CSS properties, ARIA information and JavaScript functions have been wrapped in this module to allow you to nearly to everything from Python.

No need to change code anymore or to maintain multiple static templates.
 
<div align="center" >
    <img src="https://github.com/marlyk/epyk-uvicorn/blob/master/static/images/server_archi_2.PNG?raw=true">
</div>


On teh server side for complex component, the data module will provide you with simple function to convert the data to the right format.

<div align="center" >
    <img src="https://github.com/marlyk/epyk-uvicorn/blob/master/static/images/server_archi_3.PNG?raw=true">
</div>

Benefits
================================

- No need anymore to maintain multiple folder with various styles and template. This can be managed by inheritance directly on the Python Layer.
- No need to install or import the right modules to your app. Components will build the page and add dynamically the necessary external packages.
- No need to reimplement / restructure your templates based on the target server (inddeed this will have multiple output to adpatd according to the target server)


Do not hesitate to propose new examples !