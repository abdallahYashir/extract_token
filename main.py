import pyperclip


def copy_from_clipboard():
    return pyperclip.waitForPaste()
    # return pyperclip.waitForNewPaste()


def copy_to_clipboard(content):
    pyperclip.copy(content)


def extract_bearer_token(content):
    if "Authorization: Bearer " in content:
        header, token = content.split("Authorization: Bearer ")
        return token[0:len(token) - 1].strip()
    return None


if __name__ == '__main__':
    content = copy_from_clipboard()
    token = extract_bearer_token(content)
    copy_to_clipboard(token)
