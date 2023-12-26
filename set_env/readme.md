# Install Node.js
* https://nodejs.org
* Node.js 설치

# Install Svelte
* 프로젝트 디렉토리로 이동(cmd)
* 프로젝트 가상환경 activate
* svelte 애플리케이션을 위한 저장환경 구성

```
(cmd)npm create vite@latest frontend -- --template svelte
```

* svelte 애플리케이션 설치

```
(cmd)cd frontend
```

```
npm install
```

* VSCode에서 'Svelte for VSCode' 설치
    * https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode
* 자바스크립트 타입 체크 설정 끄기
    * VSCode에서 jsconfig.json 파일을 아래와 같이 수정
    ```
    {
        "compilerOptions": {
            (생략)
            "checkJs": false
        }
    }
    ```

# Svelte 서버 실행
* 서버실행
```
npm run dev
```