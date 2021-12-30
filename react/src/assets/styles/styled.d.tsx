import "styled-components";

export const CssData = {

  /* ========== Colors ========== */
  BodyColor: "#fbfefd",
  TextColor: "#707070",
  TextShadow: "#252525",
  TitleColor: "#393939",
  FooterColor: "#C4C4C4",
  FooterText : "#000000",
  ScrollColor: "#bd1313",
  FirstColor: "#535353",
  FirstColorAlt: "#787575",  
  TextColorLight: "#a6a6a6",
  ContainerColor: "#ffffff",
  ButtonColor: "#C4C4C4",
  ActiveColor: "#bd1313",

  /* ========== Sizes ========== */
  h1Fontsize: "1.5rem",
	h2Fontsize: "1.35rem",
	h3Fontsize: "1.2rem",
  BiggestFontSize: "2rem",
  NormalFontSize: "0.938rem",
  SmallFontSize: "0.813rem",
  SmallerFontSize: "0.75rem",
  mb1: "0.5rem",
  mb2: "1rem",
  mb3: "1.5rem",
  mb4: "2rem",
  mb5: "2.5rem",
  mb6: "3rem",
  mb7: "5rem",
  FontMedium: 400,
	FontSemiBold: 600,

  /* ========== Colors ========== */
  MaxWidth: "1020px",

  /*========== Margenes ==========*/
  HeaderHeight: "3rem",
  HeaderHeightAdd: "5rem",
  NaverMapHeight: "5rem",
  
  // /*========== Font and typography ==========*/
  BodyFont: 'Noto Sans KR',
  
  // /*========== z index ==========*/
  // z-tooltip: 10;
  // z-fixed: 100;
}
export default CssData;


declare module "styled-components" {
  export interface DefaultTheme {
    basicWidth: string;
    color: {
      main: string;
      sub: string;
    };
  }
};