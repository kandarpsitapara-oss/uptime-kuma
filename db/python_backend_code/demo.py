<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <title>LinkedIn Colleague Search</title>
  <style type="text/css" media="screen">
    html, body, div, span, applet, object, iframe,
    h1, h2, h3, h4, h5, h6, p, blockquote, pre,
    a, abbr, acronym, address, big, cite, code,
    del, dfn, em, font, img, ins, kbd, q, s, samp,
    small, strike, strong, sub, sup, tt, var,
    dl, dt, dd, ol, ul, li,
    fieldset, form, label, legend,
    table, caption, tbody, tfoot, thead, tr, th, td {
      margin: 0;
      padding: 0;
      border: 0;
      outline: 0;
      font-weight: inherit;
      font-style: inherit;
      font-size: 100%;
      font-family: inherit;
      vertical-align: baseline;
    }
    
    /* remember to define focus styles! */
    :focus {
      outline: 0;
    }
    body {
      line-height: 1;
      color: black;
      background: white;
    }
    ol, ul {
      list-style: none;
    }
    /* tables still need 'cellspacing="0"' in the markup */
    table {
      border-collapse: separate;
      border-spacing: 0;
    }
    caption, th, td {
      text-align: left;
      font-weight: normal;
    }
    blockquote:before, blockquote:after,
    q:before, q:after {
      content: "";
    }
    blockquote, q {
      quotes: "" "";
    }
  </style>
  <style type="text/css" media="screen">
    #body {
      margin: 0 auto;
    }
    
    .wrapper {
      background-color: white;
      padding: 20px;
      width: 252px;
      -moz-box-shadow: 0 0 10px 4px #888;
    }
    
    .title {
      font-weight: bold;
      font-size: 1.2em;
      height: 30px;
    }
    
    .inputs {
      height: 30px;
      width: 252px;
      padding-bottom: 10px;
    }
    
    #keywords {
      border: 1px solid #ccc;
      padding: 3px 5px 1px;
      width: 217px;
      height: 17px;
      -moz-border-radius: 3px 0px 0px 3px;
    }
    
    #search {
      -moz-border-radius: 0px 3px 3px 0px;
      background: url("http://static02.linkedin.com/scds/common/u/img/sprite/sprite_global_v5.png") no-repeat scroll -9px -1199px #0076A8;
      border: 1px solid #06598B;
      color: #0076A8;
      cursor: pointer;
      height: 23px;
      width: 19px;
      text-indent: -9999px;
      left: -4px;
      position: relative;
    }
    
    ul.user-list {
      list-style: none;
      width: 252px;
    }
    
    li.user {
      float: left;
      height: 61px;
      width: 61px;
      position: relative;
      margin-right: 2px;
      margin-bottom: 2px;
    }
