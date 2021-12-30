// src/assets/styles/global-styles.ts
import { createGlobalStyle } from "styled-components";
import { normalize } from "styled-normalize";

// 위에서 받은 `normalize`로 기본 css가 초기화 합니다.
const GlobalStyle = createGlobalStyle`

  ${normalize}

  * {
    font-family: 'Noto Sans KR', sans-serif;
  }

  .navbarhidden {
    height: -100px;
    display:none;
    transition: 1s;
  }


  /* react-image-gallery style css */
  .image-gallery {
    /* padding-top: 90px; */
    /* width: 40%; */
    /* height: auto; */
    margin: auto;
    /* align-items: center; */
    /* width: 100vw; */
    /* padding: 50px; */
    /* justify-content: center; */
  }

  .image-gallery-slide img {
    width: 100%;
    height: auto;
    max-height: 80vh;
    object-fit: cover;
    overflow: hidden;
    object-position: center center;
    }

  .fullscreen .image-gallery-slide img {
    max-height: 100vh;
  }
`
export default GlobalStyle;