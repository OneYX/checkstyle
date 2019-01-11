# checkstyle
### Java代码规范之CheckStyle + Git Hook

- 本地代码提交前checkstyle & 注释规范检查
- 依赖环境：python（2.7版本）

```sh
git config --add checkstyle.jar config/checkstyle-8.9.jar
git config --add checkstyle.checkfile config/check_style.xml
cp config/pre-commit ./.git/hooks/
cp config/check.py ./.git/hooks/
```

