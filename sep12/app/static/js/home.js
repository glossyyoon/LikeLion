/* 
첫 번째로 api에서 받은 key, default 날짜로 구성된 url을 임의로 설정하고 
해당 일자의 rank 데이터를 받아 html에 전송해주는 기초적인 과정을 다뤄볼게요
< Contents >
1. key 받아와 날짜정보를 임의로 작성해서 url로 보내주기
2. async & await & promise object 맛보기
3. rank 데이터 받아서 html에 쏴주기 
*/
let lastDay = new Date(new Date() - 1000 * 60 * 60 * 24)
  .toISOString()
  .substring(0, 10);
let dateInput = document.querySelector('.todayDateInput');
dateInput.value = lastDay;
dateInput.setAttribute('max', lastDay);
let contentsBox = document.querySelector('.contents'); // 그냥 html에 있는 class contents div

const clickedSearchBtn = async () => {
  await giveRankObject()
    .then((data) => {
      let DtYear = data.boxOfficeResult.showRange.substring(0, 4);
      let DtMonth = data.boxOfficeResult.showRange.substring(4, 6);
      let DtDate = data.boxOfficeResult.showRange.substring(6, 8);
      // 20200906~20200906 형태에서 원하는 부분만 잘랐어요
      // 더 간략하게 할 수 있을거 같은데 일단 이렇게!
      let dateTitle = document.createTextNode(
        `${DtYear}년 ${DtMonth}월 ${DtDate}일 박스 오피스`
      );
      //appenchild해주기 위해 textnode로 담아 주시고
      let titleBox = document.createElement('h1');
      // h1 태그도 하나 만들어주시고
      let createDiv = document.createElement('div');
      //div도 만들어주시고
      createDiv.classList.add('moviePackage');
      // 만든 div 클래스에 moviePackage 를 추가해 주시고
      contentsBox
        .appendChild(createDiv)
        .appendChild(titleBox)
        .appendChild(dateTitle);
      // contentsBox 속에 만든 div 그 속에 titleBox(h1 태그) h1태그 글자를 dateTitle로 해줍시다.
      for (let i = 0; i < 10; i++) {
        let movieRankJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieNm;
        let text = document.createTextNode(`${i + 1}위 ` + movieRankJson);
        //~~위 를 표시하기 위해 `${i+1}위 `를 추가했어요
        let textBox = document.createElement('p');
        // p태그 만들어주시고
        contentsBox
          .appendChild(createDiv)
          .appendChild(titleBox)
          .appendChild(dateTitle);
        textBox.setAttribute('value', `${movieRankJson}`);
        textBox.setAttribute('onclick', 'showMeTheCode(this)');

        // contentsBox 속에 만든 div 그 속에 textBox(p 태그) p태그 글자를 text(~위 영화제목)로 해줍시다.
      }
    })
    .catch((error) => console.log(`에러 발생 ${error.name}:${error.message}`));
};

const giveRankObject = async () => {
  let date = document.todayDateForm.todayDateInput.value;
  let targetDate = date.replaceAll('-', '');
  const key = '?key=939b44eaa2fa476e3679af34204fb381';
  let targetTodayDate = `&targetDt=${targetDate}`; // 검색형식이에요
  const url =
    'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json' +
    key +
    targetTodayDate; // 검색할 json파일 url 입니다
  const response = await fetch(url);
  return await response.json();
};

const showMeTheCode = async (clickedValue) => {
  console.log(clickedValue);
  let iWantedValue = clickedValue.value;
  console.log(iWantedValue);
};
