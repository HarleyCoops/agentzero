import wolframalpha

# Your Wolfram Alpha App ID
app_id = 'K8A2GH-V499THQ4QR'  # Replace with your actual App ID
client = wolframalpha.Client(app_id)

# Function to ask Wolfram Alpha
def ask_wolfram(question):
    try:
        res = client.query(question)
        answer = next(res.results).text
        return answer
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    # Read all text from the specified path
    with open(r'C:\Users\admin\agentzero\prompts\prompt.txt', 'r') as file:
        question = file.read()  # Read the entire file as a single string

    # Send the entire content as a single prompt
    answer = ask_wolfram(question)
    print(f'Question: {question}\nAnswer: {answer}\n')