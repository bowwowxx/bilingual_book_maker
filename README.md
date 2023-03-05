這東西真是太酷了，~難怪一堆人fork~ 
- 新增Google Colab Notebooks直接Mount GoogleDrive轉書
- 直接翻譯語系為繁體
- 測試剛出的model:gpt-3.5-turbo-0301 
- 新增加pptx翻譯(求生存用)
- 增加test.py測試OpenAI Model用

Google Colab Notebooks(可自行取用):  
https://colab.research.google.com/drive/1DH9h1ySD5sOFWWNNO2oY4mWBF_SQwpG4

```shell
export OPENAI_API_KEY=${your_api_key}

python3 make_pptx.py -f pptx/samplepptx.pptx
python3 make_book.py --book_name test_books/animal_farm.epub --model gpt3 --no_limit
```

---------------

**[中文](./README-CN.md) | English**

# bilingual_book_maker
Make bilingual epub books Using AI translate

![image](https://user-images.githubusercontent.com/15976103/222317531-a05317c5-4eee-49de-95cd-04063d9539d9.png)


## Preparation

1. ChatGPT or OpenAI token
2. prepared epub books
3. Environment with internet access or proxy
4. python3.8+


## Use

1. pip install -r requirements.txt
2. OpenAI API key. If you have multiple keys, separate them by commas (xxx,xxx,xxx) to reduce errors caused by API call limits.
3. A sample book, test_books/animal_farm.epub, is provided for testing purposes.
4. A sample book, animal_farm.epub, is provided for testing purposes.
5. Use --test command to preview the result if you haven't paid for the service. Note that there is a limit and it may take some time.
6. Set the target language like `--language "Simplified Chinese"`. 
   Suppot ` "Japanese" / "Traditional Chinese" / "German" / "French" / "Korean"`.
   Default target language is `"Simplified Chinese"`. Support language list please see the LANGUAGES at [utils.py](./utils.py).
7. Use the --proxy parameter to enable users in mainland China to use a proxy when testing locally. Enter a string such as http://127.0.0.1:7890.
8. Use the --resume command to manually resume the process after an interruption.

e.g.
```shell
# Test quickly
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --no_limit --test --language "Simplified Chinese"
# or do it
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --language "Simplified Chinese"
# or use the GPT-3 model
export OPENAI_API_KEY=${your_api_key}
python3 make_book.py --book_name test_books/animal_farm.epub --model gpt3 --no_limit --language "Simplified Chinese"
```

## Notes

1. here is a limit. If you want to speed up the process, consider paying for the service or use multiple OpenAI tokens
2. PR welcome
3. The DeepL model will be updated later.


# Thanks

- @[yetone](https://github.com/yetone)

# Contribution

- Any issues or PRs are welcome.
- TODOs in the issue can also be selected.
- Please run black make_book.py before submitting the code.

## Appreciation

Thank you, that's enough.

![image](https://user-images.githubusercontent.com/15976103/222407199-1ed8930c-13a8-402b-9993-aaac8ee84744.png)
