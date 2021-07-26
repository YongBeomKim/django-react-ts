import React from "react";
import styles from './Welcome.module.css'
import sytled from 'styled-components';

// Part 1
// Style 및 변수처리 
const Title = sytled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`

export default function Welcome() {

  const name = "Python"
  const naver = {
    name : "Naver",
    url : "http://naver.com",
  }

  return(
    // jsx 템플릿은 1개의 Div 만 출력가능
    <>
      <Title>Hello {name} <span>{name+10}</span></Title>
      <div className={styles.box}>Hello</div>
      <a href={naver.url}>{naver.name}</a>
      <Title>Title Text</Title>
    </>
  )
}