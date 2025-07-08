# 🧾 Git Convention

`Type`을 활용한 `Git Convention`

## 🎯 목적

Issue, Pull Request, Commit Message, Branch에 일관된 `[Type]` 포맷을 적용하여

자동 라벨링 및 변경 이력을 명확히 관리합니다.

## 🧩 적용 대상

- ✅ Issue 제목
  - `.github/ISSUE_TEMPLATE` 참고
- ✅ Pull Request 제목
  - `.github/PULL_REQUEST_TEMPLATE.md` 참고
- ✅ Commit Message Header
  - `.commit_template.txt` 참고
  - `git config commit.template .commit_template.txt`
- ✅ Branch 이름
  - `Feat/{issue number}-{short description}`
  - 예시: `Feat/123-add-login-page`

## 🔧 자동 라벨링 사용 도구

- GitHub Action: [srvaroa/labeler](https://github.com/srvaroa/labeler)

### 📌 참고

- `labeler`는 PR 제목 또는 Issue 제목에 포함된 **정규식 매칭**으로 동작합니다.

* PR 제목은 `Template`에서 설정할 수 없어, 사용자가 직접 작성해야 합니다
* PR 템플릿 내에 `[Type]` 사용 가이드를 명시해두어야 정확하게 작동합니다.

## 🧾 Type List

| Type         | 설명                  |
| ------------ | --------------------- |
| `[Feat]`     | 기능 추가             |
| `[Bug]`      | 버그 수정             |
| `[Refactor]` | 리팩토링 (기능 유지)  |
| `[Docs]`     | 문서 수정             |
| `[Build]`    | 빌드 관련 작업        |
| `[CI/CD]`    | 배포 및 자동화 설정   |
| `[Chore]`    | 기타 작업 (빌드 제외) |
| `[Enhance]`  | 기능 개선             |
