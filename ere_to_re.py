import sys;

args = sys.argv[1:]


def remove_terminating_sequence(ere: str):
    return

def implicit_creation_events(ere: str):
    return

def replace_epsilon_events(ere: str):
    return

def create_anonymization(ere:str):
    '''
    Generates and applies a mapping of the events to unique characters.
    This is done as regex comparison tools view "event" as 5 seperate entities, first the letter e,
    then the letter v, and so on.
    In ERE for TraceMOP, "event" is a single entity.
    The number of unique events is limited to 26 using this algorithm, the capital letters of the alphabet.
    The special epsilon events will be replaced with the "~", a character.
    '''
    ere += " "

    curr_replacement = "A"
    curr_event = ""
    event_dict = {"epsilon":"~"}
    new_ere = ""

    valid_char = [*range(ord('a'), ord('z')+1), *range(ord('0'), ord('9')+1), ord("_")]
    for c in ere:
        if ord(c) in valid_char:
            curr_event += c
        else:
            if curr_event:
                if curr_event in event_dict:
                    new_ere += event_dict[curr_event]
                else:
                    event_dict[curr_event] = curr_replacement
                    new_ere += curr_replacement
                    curr_replacement = chr(ord(curr_replacement)+1)

                curr_event = ""

            new_ere += c
    return new_ere, event_dict
def use_anonymization(ere:str, anonymization_map:dict):
    '''
    Uses the mapping generated from create_anonymization to replace the events
    with single unique characters.
    If an event in this ere is not in the anonymization_map, it replaces them starting with the lowercase alphabet.
    '''
    ere += " "

    curr_event = ""
    new_ere = ""
    curr_replacement = "a"

    valid_char = [*range(ord('a'), ord('z') + 1), *range(ord('0'), ord('9') + 1), ord("_")]
    for c in ere:
        if ord(c) in valid_char:
            curr_event += c
        else:
            if curr_event:
                if curr_event not in anonymization_map:
                    anonymization_map[curr_event] = curr_replacement
                    new_ere += curr_replacement
                    curr_replacement = chr(ord(curr_replacement)+1)
                    curr_event = ""
                else:
                    new_ere += anonymization_map[curr_event]
                    curr_event = ""
            new_ere += c
    return new_ere
def standardize_ere_specs(ere1: list, ere2: list):
    ere1_string, anom_dict = create_anonymization(ere1[0].lower())
    ere2_string = use_anonymization(ere2[0].lower(), anom_dict)

    return ere1_string, ere2_string

if __name__ == "__main__":
    generated_ere_file = args[0]
    ground_truth_ere_file = args[1]

    f = open(generated_ere_file, 'r')
    generated_ere_list = []
    for l in f.readlines():
        generated_ere_list.append(l)
    f.close()

    f = open(ground_truth_ere_file, 'r')
    ground_truth_ere_list = []
    for l in f.readlines():
        ground_truth_ere_list.append(l)
    f.close()

    '''
    Each line in both files should be of format "{ERE};{Match/Fail};{List of Creation Events}"

    For example, for the Socket_InputStreamUnavailable specification 
    (https://github.com/SoftEngResearch/tracemop/blob/master/scripts/props/Socket_InputStreamUnavailable.mop)

    (create_connected | create_unconnected connect) get* (close | shutdown)*;fail;create_connected,create_unconnected
    '''

    n = len(generated_ere_list)
    generated_ere_new = []
    ground_truth_ere_new = []

    for i in range(n):
        generated_ere = generated_ere_list[i].split(";")
        ground_truth_ere = ground_truth_ere_list[i].split(";")

        a,b = standardize_ere_specs(generated_ere, ground_truth_ere)

        generated_ere_new.append(a)
        ground_truth_ere_new.append(b)

    f = open("standardized_" + generated_ere_file, 'w')
    f.write("\n".join(generated_ere_new))
    f.close()

    print("Created standardized_" + generated_ere_file + " containing standardized generated ere")
    f = open("standardized_" + ground_truth_ere_file, 'w')
    f.write("\n".join(ground_truth_ere_new))
    f.close()

    print("Created standardized_" + ground_truth_ere_file + " containing standardized ground-truth ere")

